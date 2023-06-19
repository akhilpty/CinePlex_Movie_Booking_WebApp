from django.db import models
import datetime




class Movie(models.Model):
    movie_name=models.CharField(max_length=100)
    duration = models.CharField(max_length=100,null=True)
    language=models.ManyToManyField('Movie_languages')
    genre=models.ManyToManyField('Movie_genres')
    date=models.DateField(default=datetime.date.today)
    time=models.ForeignKey('Movie_time',on_delete=models.CASCADE,null=True)
    image=models.FileField(upload_to='images')
    is_active=models.SmallIntegerField(default=1)
    trailer=models.CharField(max_length=500)
   


  
    def __str__(self):
        return self.duration

    
class Movie_time(models.Model):
    time=models.TimeField()
    def __str__(self):
        return self.time.strftime("%I:%M:%p")

class Movie_languages(models.Model):
    language=models.CharField(max_length=50)
    def __str__(self):
        return self.language
    
class Movie_genres(models.Model):
    genre=models.CharField(max_length=50)
    def __str__(self):
        return self.genre



    









    