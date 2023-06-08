from rest_framework.serializers import ModelSerializer
from .models import *


class JewelryTagSerializer(ModelSerializer):
    class Meta:
        model = JewelryTag
        fields = '__all__'


class JewelryThumnailImageSerializer(ModelSerializer):
    class Meta:
        model = JewelryThumnailImage
        fields = '__all__'


class JewelryImagesSerializer(ModelSerializer):
    class Meta:
        model = JewelryImages
        fields = '__all__'


class JewelrySerializer(ModelSerializer):
    tags = JewelryTagSerializer(many=True, read_only=True)
    images = JewelryImagesSerializer(many=True, read_only=True)
    thumbnail_images = JewelryThumnailImageSerializer(
        many=True, read_only=True)

    class Meta:
        model = Jewelry
        fields = '__all__'
