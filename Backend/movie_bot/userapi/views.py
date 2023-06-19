from django.conf import settings
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from .models import Booking, PaymentStatus
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_200_OK,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT,
    HTTP_401_UNAUTHORIZED
)
from rest_framework.permissions import AllowAny
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import red
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.shortcuts import render
from .forms import BookingModelForm, PaymentModelForm, registerUser, loginUser
from movie_admin.models import Movie
from .serailizers import BookingSerializer, MovieSerializer
import razorpay
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from django.forms.models import model_to_dict

razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
# user register


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def register_user(request):
    registerform = registerUser(request.data)
    if registerform.is_valid():
        username = registerform.cleaned_data['username']
        email = registerform.cleaned_data['email']
        password = registerform.cleaned_data['password']
        conf_password = registerform.cleaned_data['conf_password']
        if password == conf_password:
            if User.objects.filter(username=username).exists():
                registerform = registerUser(request.POST)
                context = {'registerform': registerform.data,
                           'error': 'Username already exists add a new one'}
                return Response(context, status=HTTP_400_BAD_REQUEST)
            else:
                user = User.objects.create_user(username=username,
                                                email=email,
                                                password=password,)

                user.save()
                context = {'registerform': registerform.data,
                           'success': 'Created user'}
                return Response(context, status=HTTP_200_OK)
        else:
            registerform = registerUser(request.POST)
            context = {'registerform': registerform.data,
                       'errors': "password doesnt match"}
            return Response(context, status=HTTP_400_BAD_REQUEST)
    registerform = registerUser(request.POST)
    context = {'registerform': registerform.data,
               'errors': registerform.errors}
    return Response(context, status=HTTP_400_BAD_REQUEST)


# user login
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login_user(request):
    loginform = loginUser(request.data)
    if loginform.is_valid():
        username = loginform.cleaned_data['username']
        password = loginform.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            login(request, user)
            return Response({'Token': token.key, "message": 'User is logged in', "userid": user.id}, status=HTTP_200_OK)
        else:
            return Response({"message": 'Invalid Credentials', "warning": "If problem persist contact admin"}, status=HTTP_401_UNAUTHORIZED)
    context = {'loginform': loginform.errors}
    return Response(context)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def logout_user(request):
    logout(request)
    return Response({"message": 'User is logged out'}, status=HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def usermovielist(request):
    allMovie = Movie.objects.filter(is_active=True,)
    allMovie_Serializer = MovieSerializer(allMovie, many=True)
    return Response(allMovie_Serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def usermoviedetails(request, id):
    allMovie = Movie.objects.filter(is_active=True, id=id)
    if not allMovie.exists():
        raise Http404
    allMovie_Serializer = MovieSerializer(allMovie, many=True)
    return Response(allMovie_Serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def booking_model_view(request, id):
    user = request.user
    
    form = BookingModelForm(request.data)
   
    if form.is_valid():
        seat = form.cleaned_data["seat"]
        price = form.cleaned_data["price"]
        count = form.cleaned_data["count"]
        language = form.cleaned_data["language"]
        movie_details = Movie.objects.get(id=id)

        total_amount = price * count
       
        print(total_amount)

        booking = Booking.objects.create(
            user_id=user,
            movie_id=movie_details,
            seat=seat,
            price=price,
            count=count,
            total_amount=total_amount,
            language=language

        )

        return Response({'success': 'Booking created'}, status=HTTP_200_OK)
    else:
        return Response({'form': form.errors}, status=HTTP_400_BAD_REQUEST)



@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def new_order(request, id):
    if request.method == "GET":

        data = Booking.objects.filter(movie_id=id).order_by('-id').first()
        data_id = data.id
        movie_ins = data.movie_id
        movie_name = movie_ins.movie_name
        movie_seat = data.seat
        movie_count = data.count
        movie_total = data.total_amount
        movie_price = data.price
        movie_language = data.language
        date = movie_ins.date
        time = str(movie_ins.time)
    
      

        new_order_response = razorpay_client.order.create({
            "amount": movie_total*100,
            "currency": "INR",
                        "payment_capture": "1"
        })

        response_data = {

            "razorpay_key": "rzp_test_A5y00lngBViGdQ",
            "order": new_order_response,
            "movie_name": movie_name,
            "seat": movie_seat,
            "data_id": data_id,
            "total": movie_total,
            "count": movie_count,
            'price': movie_price,
            'language': movie_language,
            'date': date,
            "time":time

        }

        return JsonResponse(response_data)


@csrf_exempt
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def order_callback(request):
    if request.method == "POST":
        paymentform = PaymentModelForm(request.data)

        if paymentform.is_valid():
            customer_details = paymentform.cleaned_data['customer_details']
            order_id = paymentform.cleaned_data['order_id']
            payment_id = paymentform.cleaned_data['payment_id']
            payment_signature = paymentform.cleaned_data['payment_signature']

            order_ins = PaymentStatus.objects.create(
                customer_details=customer_details,
                order_id=order_id,
                payment_id=payment_id,
                payment_signature=payment_signature,

            )
            order_ins.save()

            return JsonResponse({"res": "success"})
        else:
            return JsonResponse({"res": "Invalid data returned", "errors": paymentform.errors})
    else:
        return JsonResponse({"res": "Invalid request method"})


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def my_booking(request):
    current_user = request.user.id
    booking = Booking.objects.filter(
        user_id=current_user).order_by('-movie_id__date')
    serializer = BookingSerializer(booking, many=True)

    for data in serializer.data:
        movie_id = data['movie_id']
        movie = Movie.objects.get(id=movie_id)
        data['movie_name'] = movie.movie_name
        data["movie_date"] = movie.date
    return Response(serializer.data, status=HTTP_200_OK)


@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def ticket_pdf(request,angularid):
    

    pdf_model = PaymentStatus.objects.get(customer_details=angularid)

    movie_name = pdf_model.customer_details.movie_id.movie_name
    language = pdf_model.customer_details.language
    date = pdf_model.customer_details.movie_id.date
    date = date.strftime("%b %d %Y")
    time = pdf_model.customer_details.movie_id.time
    seat = pdf_model.customer_details.seat
    genres = list(pdf_model.customer_details.movie_id.genre.all())
    genre = ', '.join([str(g) for g in genres])
    price = pdf_model.customer_details.total_amount
    orderid = pdf_model.order_id
    img_file = pdf_model.qr_code.path

    # Use the img_file path as needed in your view

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="movie_ticket.pdf"'
    pagesize = ((700, 350))

    p = canvas.Canvas(response, pagesize=pagesize)

    p.setFont("Helvetica", 20)
    p.drawString(50, 270, f"Movie: {movie_name}")
    p.drawString(50, 240, f"Language: {language}")
    p.drawString(50, 210, f"Date: {date}")
    p.drawString(50, 180, f"Time: {time}")
    p.drawString(50, 150, f"Seat: {seat}")
    p.drawString(50, 120, f"Price: Rs-{price}")
    p.drawString(50, 90, f"Genre: {genre}")
    p.drawString(50, 50, f"OrderID: {orderid}")
    p.drawImage(img_file, 400, 35, width=160,
                preserveAspectRatio=True, mask='auto')

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    title_style.textColor = red
    title_style.fontName = "Helvetica-Bold"
    title_style.alignment = 1

    title_style.fontSize = 40

# Draw the "Movie Ticket" text with the custom style
    p.setFont(title_style.fontName, title_style.fontSize)
    p.setFillColor(title_style.textColor)
    p.drawCentredString(350, 300, "Movie Ticket")

    # Save the PDF
    p.showPage()
    p.save()
    return response
