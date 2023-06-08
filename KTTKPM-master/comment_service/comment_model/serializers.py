from rest_framework.serializers import ModelSerializer
from .models import *


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

