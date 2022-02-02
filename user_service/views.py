from rest_framework import viewsets
from rest_framework import status , parsers
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .permissions import IsList

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsList,)
    queryset = User.objects.all()
    serializer_class = UserSerializer