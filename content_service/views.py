from rest_framework import viewsets
from rest_framework import status , parsers
from rest_framework.permissions import IsAuthenticated
from .serializers import ContentSerializer
from .models import Content
from rest_framework.decorators import action
from rest_framework.response import Response
import pandas as pd 
from rest_framework import filters
# importing datetime module
import datetime
from django.contrib.auth import get_user_model
User = get_user_model()

class ContentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    parser_classes = [parsers.MultiPartParser,parsers.FormParser]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['publish_date', 'reads' ,"likes"]

    @action(detail=False, methods=['post'], name='POST CSV')
    def post_csv(self, request, *args, **kwargs):
        
        df = request.data['csv']
        df = pd.read_csv(df)
        print(df)
        
        for index, row in df.iterrows():
            print(row)
            title = row['title']
            story = row['story']
            publish_date = row['publish_date'] 
            publish_date = datetime.datetime.now()
            Content.objects.create( title = title , story = story , publish_date = publish_date)
            ## here we can add some try catch blocks to resolve duplicate conflict
        return Response(status=status.HTTP_201_CREATED)
