from rest_framework import permissions
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import Http404


# Create your views here.
class BlogView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        blog = Blog.objects.all()

        serializer = BlogSerializer(blog, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class BlogDetail(APIView):
    def get_object(self, id):
        try:
            return Blog.objects.get(id=id)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, id): 
        blog = get_object_or_404(Blog, id=id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        blog = self.get_object(id)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        blog = get_object_or_404(Blog, id=id)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)