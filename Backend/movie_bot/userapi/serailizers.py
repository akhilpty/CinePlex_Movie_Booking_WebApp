
from .models import Booking
from rest_framework import serializers
from movie_admin.models import Movie,Movie_genres

# Serializing data


class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField(many=True)
    language = serializers.StringRelatedField(many=True)
    time = serializers.StringRelatedField()
    class Meta:
        model = Movie
        fields=('id','movie_name','language','genre','duration','date','time','image','trailer')

class BookingSerializer(serializers.ModelSerializer):
    
   
    class Meta:
        model =Booking
        fields=("__all__")

      
