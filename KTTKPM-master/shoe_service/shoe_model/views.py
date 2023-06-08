from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .models import *
from .serializers import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def getShoes(request):
    Shoes = Shoe.objects.all()
    serializer = ShoeSerializer(Shoes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getShoe(request, id):
    Shoes = Shoe.objects.get(id=id)
    serializer = ShoeSerializer(Shoes, many=False)
    return Response(serializer.data)
