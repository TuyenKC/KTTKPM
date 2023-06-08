from rest_framework.serializers import ModelSerializer
from .models import *


class BookTagSerializer(ModelSerializer):
    class Meta:
        model = BookTag
        fields = '__all__'


class BookThumnailImageSerializer(ModelSerializer):
    class Meta:
        model = BookThumnailImage
        fields = '__all__'


class BookImagesSerializer(ModelSerializer):
    class Meta:
        model = BookImages
        fields = '__all__'


class BookSerializer(ModelSerializer):
    tags = BookTagSerializer(many=True, read_only=True)
    images = BookImagesSerializer(many=True, read_only=True)
    thumbnail_images = BookThumnailImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
