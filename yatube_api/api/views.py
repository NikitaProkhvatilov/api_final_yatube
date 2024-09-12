from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets

from posts.models import Post, Group
from .serializers import (PostSerializer,
                          CommentSerializer,
                          GroupSerializer,
                          FollowSerializer)
from .permissions import IsAuthorOrAutheticated


class PostViewSetAndDetail(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrAutheticated, ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSetAndDetail(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrAutheticated, ]

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_pk'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user,
                        post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user__username', '=following__username')

    def get_queryset(self):
        return self.request.user.followers.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
