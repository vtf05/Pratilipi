from django.db import models
from django.utils import timezone
# Create your models here.
class Content(models.Model) :
    title = models.CharField(blank = False , max_length=200)
    story = models.TextField(blank = False)
    likes  = models.IntegerField(default = 0 )
    reads  = models.IntegerField(default = 0 )
    publish_date = models.DateTimeField( )
