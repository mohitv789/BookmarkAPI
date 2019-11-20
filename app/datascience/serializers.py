from core.models import MachineLearningModel, MachineLearningModelType
from rest_framework import serializers


class MachineLearningModelTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model=MachineLearningModelType
        fields=('id','type')
        read_only_fields=('id',)

class MachineLearningModelSerializer(serializers.ModelSerializer):

    type = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=MachineLearningModelType.objects.all()
    )
    class Meta:
        model = MachineLearningModel
        fields = ['id','created','title','type','code','linenos','language','style','type']
        read_only_fields=('id',)
