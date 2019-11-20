from django.shortcuts import render
from rest_framework import generics
from core.models import MachineLearningModel
from datascience import serializers
from datascience.serializers import MachineLearningModelTypeSerializer,MachineLearningModelSerializer
from rest_framework import viewsets,mixins,authentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

class MachineLearningModelViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    queryset=MachineLearningModel.objects.all()
    serializer_class = serializers.MachineLearningModelSerializer
    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    def get_queryset(self):
        """Return objecs for the current authenticated user only"""
        """From now filtering is implemented"""
        created_by = self.request.query_params.get("created_by")
        queryset = self.queryset
        return queryset.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
