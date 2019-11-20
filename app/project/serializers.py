from core.models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id','created','title','tag','code','language','linenos','language','style']
        read_only_fields=('id',)
