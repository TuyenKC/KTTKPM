from rest_framework.serializers import ModelSerializer
from .models import *


class ShoeTagSerializer(ModelSerializer):
    class Meta:
        model = ShoeTag
        fields = '__all__'


class ShoeThumnailImageSerializer(ModelSerializer):
    class Meta:
        model = ShoeThumnailImage
        fields = '__all__'


class ShoeImagesSerializer(ModelSerializer):
    class Meta:
        model = ShoeImages
        fields = '__all__'


class ShoeSerializer(ModelSerializer):
    tags = ShoeTagSerializer(many=True, read_only=True)
    images = ShoeImagesSerializer(many=True, read_only=True)
    thumbnail_images = ShoeThumnailImageSerializer(many=True, read_only=True)

    class Meta:
        model = Shoe
        fields = '__all__'
