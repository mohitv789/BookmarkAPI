from django.shortcuts import render
from rest_framework import generics
from core.models import Post
from post import serializers
from post.serializers import PostSerializer
from rest_framework import viewsets,mixins,authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class PostViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    queryset=Post.objects.all()
    serializer_class = serializers.PostSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    def _params_to_ints(self,qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        """Return objecs for the current authenticated user only"""
        """From now filtering is implemented"""
        queryset = self.queryset
        return queryset

    def perform_create(self,serializer):
        """Create a new recipe object"""
        serializer.save(posted_by=self.request.user)
