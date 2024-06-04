# from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
# from rest_framework.throttling import AnonRateThrottle

from posts.models import Post, Comment, Like
from posts.serializers import PostSerializer, CommentSerializer, LikeSerializer, PostLessDataSerializer
from posts.permissions import IsOwnerOrReadOnly

# Create your views here.

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    # throttle_classes = [AnonRateThrottle]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def list(self, request, *args, **kwargs):
        queryset = Post.objects.all().only("id", "text", "image", "created_at")
        serializer = PostLessDataSerializer(queryset, many=True)
        return Response(serializer.data)
        

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        post_id = self.kwargs["id"]
        queryset = Comment.objects.filter(post__id=post_id)
        return queryset
        
        
class LikeViewSet(ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        post_id = self.kwargs["id"]
        queryset = Like.objects.filter(post__id=post_id)
        return queryset