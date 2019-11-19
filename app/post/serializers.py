from core.models import Post, User
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    # posted_by = serializers.PrimaryKeyRelatedField(
    #     many=True,
    #     queryset=User.objects.get()
    # )
    class Meta:
        model = Post
        fields = ['id','created', 'title', 'code', 'linenos', 'language', 'style']
        read_only_fields=('id',)
