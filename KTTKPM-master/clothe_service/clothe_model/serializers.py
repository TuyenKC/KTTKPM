from rest_framework.serializers import ModelSerializer
from .models import *


class ClotheTagSerializer(ModelSerializer):
    class Meta:
        model = ClotheTag
        fields = '__all__'


class ClotheThumnailImageSerializer(ModelSerializer):
    class Meta:
        model = ClotheThumnailImage
        fields = '__all__'


class ClotheImagesSerializer(ModelSerializer):
    class Meta:
        model = ClotheImages
        fields = '__all__'


class ClotheSerializer(ModelSerializer):
    tags = ClotheTagSerializer(many=True, read_only=True)
    images = ClotheImagesSerializer(many=True, read_only=True)
    thumbnail_images = ClotheThumnailImageSerializer(many=True, read_only=True)

    class Meta:
        model = Clothe
        fields = '__all__'
