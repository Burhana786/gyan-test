from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Film,Review



# class UserModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['username','password','email']
#     def create(self,validated_data):
#         print(validated_data)
#         return User.objects.create_user(**validated_data)
    

class FilmModelSer(serializers.ModelSerializer):
    class Meta:
        model=Film
        fields="__all__"



class ReviewSerializer(serializers.ModelSerializer):
    film=FilmModelSer(many=False,read_only=True)
    class Meta:
        model=Review
        fields=['review','rating','date','film']
    def create(self,validated_data):
        # user=self.context.get("user")
        film=self.context.get("film")
        return Review.objects.create(film=film,**validated_data)
    
    def validate(self,data):
        rtng=data.get("rating")
        if rtng<0 & rtng>5:
            raise serializers.ValidationError
        return data
    