from core.models import Project,ProjectType
from rest_framework import serializers


class ProjectTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model=ProjectType
        fields=('id','type')
        read_only_fields=('id',)

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id','created','title','description','tag','linenos','language','style']
        read_only_fields=('id',)
