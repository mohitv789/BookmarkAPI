from core.models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id','created', 'title','body']
        read_only_fields=('id',)
