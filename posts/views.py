from django.shortcuts import render
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics, permissions
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    """Listing the posts to view, update and delete"""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """View, delete and update a single post"""

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
