from django.shortcuts import render
from .models import Post,Comment
from .serializers import CommentSerializer,PostSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
# Create your views here.


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDetailAPIView(APIView):
    def get(self, request, format=None):
        req = request.data.get('id') or "1"
        queryset = get_object_or_404(Post, id=req)
        serializer_class = PostSerializer(instance=queryset)
        queryset_comment = Comment.objects.filter(post=queryset)
        serializer_class_comment = CommentSerializer(instance=queryset_comment)
        data = {
            "post":serializer_class.data,
            "comments":serializer_class_comment.data
        }
        return Response(data)
    
class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer