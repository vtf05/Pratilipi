from django.db import models
from content_service.models import Content
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Like(models.Model) :
    liked_by = models.OneToOneField(User , on_delete = models.CASCADE)
    post = models.ForeignKey(Content,on_delete=models.CASCADE,related_name='like')
   

class Read(models.Model) :
    read_by =  models.OneToOneField(User , on_delete = models.CASCADE)
    post = models.ForeignKey(Content,on_delete=models.CASCADE,related_name='read')
