from django.shortcuts import render
from rest_framework import generics
from core.models import Post
from post import serializers
from post.serializers import PostSerializer
from rest_framework import viewsets,mixins,authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

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
        posted_by = self.request.query_params.get("posted_by")

        queryset = self.queryset

        return queryset.filter(posted_by=self.request.user)
    # def get_serializer_class(self):
    #     """Return appropiate serializer class"""
    #     if self.action=="retrieve":
    #         return serializers.PostSerializer
    #     elif self.action == 'upload_image':
    #         return serializers.RecipeImageSerializer
    #     return self.serializer_class
    def perform_create(self,serializer):
        """Create a new recipe object"""
        serializer.save(user=self.request.user)
    
    # @action(methods=['POST'], detail=True, url_path='upload-image')
    # def upload_image(self, request, pk=None):
    #     """Upload an image to a recipe"""
    #     recipe = self.get_object()
    #     serializer = self.get_serializer(
    #         recipe,
    #         data=request.data
    #     )
    #
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(
    #             serializer.data,
    #             status=status.HTTP_200_OK
    #         )
    #
    #     return Response(
    #         serializer.errors,
    #         status=status.HTTP_400_BAD_REQUEST
    #     )
