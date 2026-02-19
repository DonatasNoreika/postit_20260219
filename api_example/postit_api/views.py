from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post, Comment, PostLike, CommentLike
from rest_framework import generics, permissions

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



