from rest_framework import viewsets
from rest_framework import status , parsers
from rest_framework.permissions import IsAuthenticated
from .serializers import LikeSerializer  , ReadSerializer 
from .models import Like , Read
from rest_framework.decorators import action
from rest_framework.response import Response
from content_service.models import Content
# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        content_obj = Content.objects.get(id = request.data['post'])
        content_obj.likes = content_obj.likes+1 
        content_obj.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        content_obj = Content.objects.get(id = request.data['post'])
        content_obj.likes = content_obj.likes+1 
        content_obj.save()
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class ReadViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Read.objects.all()
    serializer_class = ReadSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        content_obj = Content.objects.get(id = request.data['post'])
        content_obj.likes = content_obj.likes+1 
        content_obj.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)



    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        content_obj = Content.objects.get(id = request.data['post'])
        content_obj.reads = content_obj.reads+1 
        content_obj.save()
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
       
