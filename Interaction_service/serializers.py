from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Like ,Read 

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Like 
        fields = '__all__'

class ReadSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Read
        fields = '__all__'        