from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Content



class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('title','story','publish_date')


