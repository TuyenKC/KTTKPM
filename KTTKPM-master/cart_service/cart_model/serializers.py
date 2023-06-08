from rest_framework.serializers import ModelSerializer
from .models import *

class CartItemSerializer(ModelSerializer):
    itemURL = serializers.CharField()
    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = '__all__'