from django.db import models
from django.contrib.auth.models import User
from PIL import Image, ImageDraw
import qrcode
from django.core.files import File
from io import BytesIO
from django.core.files.base import ContentFile


class Booking(models.Model):
    user_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(
        "movie_admin.Movie", on_delete=models.CASCADE, null=True)
    seat = models.CharField(max_length=100)
    price = models.FloatField(max_length=30, null=True)
    count = models.IntegerField(null=True)
    total_amount = models.IntegerField(null=True)
    language = models.CharField(null=True, max_length=50)


class PaymentStatus(models.Model):
    customer_details = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True)
    order_id = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)
    payment_signature = models.CharField(max_length=100, null=True)
    paydone = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def save(self, *args, **kwargs):
        movie = self.customer_details.movie_id
        movie_name = movie.movie_name
        movie_time = movie.time
        movie_date = movie.date
        movie_date= movie_date.strftime("%b %d %Y")
        movie_seat = self.customer_details.seat
        movie_count = self.customer_details.count
        movie_price = self.customer_details.total_amount
        movie_lang = self.customer_details.language

        movie_details = f"Name: {movie_name}\nTime: {movie_time} \n Date: {movie_date} \n Seat: {movie_seat} \n For: {movie_count} \n Total price :{movie_price} \n Language : {movie_lang}"

        try:
            qr_code = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr_code.add_data(movie_details)
            qr_code.make(fit=True)

            qr_image = qr_code.make_image(
                fill_color="black", back_color="white")

    
            qr_image = qr_image.resize((300, 300), Image.ANTIALIAS)

           
            qr_offset = Image.new("RGB", (310, 310), "white")

          
            qr_offset.paste(qr_image, (5, 5))

            file_name = f"{movie_name}-{self.customer_details.language}-qr.png"
            stream = BytesIO()
            qr_offset.save(stream, "PNG")
            self.qr_code.save(file_name, ContentFile(
                stream.getvalue()), save=False)
            stream.seek(0)
            qr_offset.close()

            super().save(*args, **kwargs)

        except Exception as e:
            
            print(f"Error generating QR code: {e}")
