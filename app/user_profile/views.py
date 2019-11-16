from rest_framework import generics,authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.reverse import reverse
from rest_framework import viewsets
from user_profile.serializers import UserSerializer,AuthTokenSerializer
from django.http import HttpResponse, JsonResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from core.models import Post, User
from user_profile.serializers import PostSerializer
from django.contrib.auth.models import User
from user_profile.serializers import UserSerializer
from user_profile.permissions import IsOwnerOrReadOnly
from django.contrib.auth import get_user_model


User = get_user_model()

class CreateUserView(generics.CreateAPIView):
    """Creates a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user!"""
    serializer_class=AuthTokenSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class=UserSerializer
    authentication_classes=(authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user


class PostList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user_profile:users', request=request, format=format),
        'posts': reverse('user_profile:posts', request=request, format=format)
    })

class PostHighlight(generics.GenericAPIView):
    queryset = Post.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(post.highlighted)

"""Mostly below would never be used or would be used logically after understanding permissions."""


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
