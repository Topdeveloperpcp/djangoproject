from .serializers import UploadSerializer
from .models import Upload
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



@permission_classes((permissions.AllowAny,))
class UploadView(APIView):
    
    def get(self, request, *args, **kwargs):
        uploads = Upload.objects.all()
        serializer = UploadSerializer(uploads, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        uploads_serializer = UploadSerializer(data=request.data)
        if uploads_serializer.is_valid():
            uploads_serializer.save()
            return Response(uploads_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', uploads_serializer.errors)
            return Response(uploads_serializer.errors, status=status.HTTP_400_BAD_REQUEST)