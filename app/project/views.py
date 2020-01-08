from django.shortcuts import render
from rest_framework import generics
from core.models import Project
from project import serializers
from project.serializers import ProjectSerializer
from rest_framework import viewsets,mixins,authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class ProjectViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    queryset=Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)
    
    def get_queryset(self):
        queryset = self.queryset
        return queryset

    def perform_create(self, serializer):
        serializer.started_by = self.request.user
        serializer.save()
