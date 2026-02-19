from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post, Comment, PostLike, CommentLike
from rest_framework import generics

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

