from datetime import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Movie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test
from .forms import adminLoginForm, addMovieForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt

#login for superuser
def admin_login(request):
    message = ""
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.method == "POST":
            logadmin = adminLoginForm(request.POST)
            if logadmin.is_valid():
                email = logadmin.cleaned_data['email']
                password = logadmin.cleaned_data['password']
                if User.objects.filter(email=email).exists():
                    username = User.objects.get(email=email).username
                    user = authenticate(username=username, password=password)
                    if user is not None:
                        login(request, user)
                    return HttpResponseRedirect(reverse('home'))
                else:
                    message = "Invalid Credentials"
                    logadmin = adminLoginForm(request.POST)
                    return render(request, 'admin_login.html', {'logadmin': logadmin, 'message': message})
            else:
                message = "Form is invalid"
                logadmin = adminLoginForm(request.POST)
                return render(request, 'admin_login.html', {'logadmin': logadmin, 'message': message})
        else:
            logadmin = adminLoginForm()
        return render(request, 'admin_login.html', {'logadmin': logadmin})

#logout for superuser
def admin_logout(request):
    logout(request)
    return redirect('loginadmin')

# checking superuser
def checksuperuser(user):
    return user.is_superuser

#home page 
class Home(UserPassesTestMixin, ListView):
    model = Movie
    template_name = "home.html"
    context_object_name = 'allMovie'
    paginate_by = 8
# checking userpassed this 
    def test_func(self):
        return self.request.user.is_superuser

    def get_login_url(self):
        return 'loginadmin'


@user_passes_test(checksuperuser, login_url=reverse_lazy('loginadmin'))
def add_movie(request):
    if request.method == 'POST':
        addmovie = addMovieForm(request.POST, request.FILES)
        if addmovie.is_valid():
            addform = addmovie.save(commit=False)
            addform.save()
            addmovie.save_m2m()
            return HttpResponseRedirect(reverse('home'))
    else:

        addmovie = addMovieForm()
    return render(request, 'add_movie.html', {'addmovie': addmovie})


@user_passes_test(checksuperuser, login_url=reverse_lazy('loginadmin'))
def movie_details(request,id):
    movie_id=Movie.objects.get(id=id)
    return render(request, 'movie_detail.html', {'movie': movie_id})
   
    
    

@user_passes_test(checksuperuser, login_url=reverse_lazy('loginadmin'))
def edit_movie(request,id):
    movie_id=Movie.objects.get(id=id)
    if request.method=='POST':
        editmovie=addMovieForm(request.POST,request.FILES,instance=movie_id)
        if editmovie.is_valid():
            addform = editmovie.save(commit=False)
            addform.save()
            editmovie.save_m2m()
            return HttpResponseRedirect(reverse('home'))
    else:

        editmovie = addMovieForm(instance=movie_id)
    return render(request, 'edit_movie.html', {'editmovie': editmovie})


@user_passes_test(checksuperuser, login_url=reverse_lazy('loginadmin'))
def delete_movie(request,id):
    movie_id=Movie.objects.get(id=id)
    movie_id.delete()
    return HttpResponseRedirect(reverse('home'))


@csrf_exempt
@user_passes_test(checksuperuser,login_url = reverse_lazy('login'))
def changestatus(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        movie_id = int(request.POST['movie'])
        action = request.POST['action']
        movie_instance = Movie.objects.get(id=movie_id)
        if action == "disable":
            movie_instance.is_active = 0
        else:
            movie_instance.is_active = 1
           
        movie_instance.save()
        return JsonResponse({'result':'success'})

@user_passes_test(checksuperuser,login_url = reverse_lazy('login'))
def search_movie(request):
    search=request.GET['search']
    fdate = request.GET.get('firstdate')
    ldate = request.GET.get('secounddate')
    movie = Movie.objects.filter(movie_name__icontains=search) 
    if fdate and ldate:
        try:
            fdate = datetime.fromisoformat(fdate).date()
            ldate = datetime.fromisoformat(ldate).date()
            movie = movie.filter(date__range=[fdate, ldate])
        except ValueError:
            pass

    return render(request, 'searchmovie.html', {'movie': movie})   



@csrf_exempt
@user_passes_test(checksuperuser,login_url = reverse_lazy('login'))
def user_status(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        user_id = int(request.POST['user'])
        action = request.POST['action']
        user_instance = User.objects.get(id=user_id)
        if action == "disable":
            user_instance.is_active = 0
        else:
            user_instance.is_active = 1
           
        user_instance.save()
        return JsonResponse({'result':'success'})
@user_passes_test(checksuperuser,login_url = reverse_lazy('login'))
def all_user(request):
    users=User.objects.all()
    return render(request, 'alluser.html',{'users':users})
