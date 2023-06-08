from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = {
        "data": "test data"
    }
    return Response(routes)
# Account
@api_view(['GET'])
def getAccounts(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getAccount(request, id):
    account = Account.objects.get(id = id)
    serializer = AccountSerializer(account, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createAccount(request):
    data = request.data
    serializer = AccountSerializer(data=data, many=False)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def loginAccount(request):
    data = request.data
    account = Account.objects.get(username = data['username'])
    if(data['password'] == account.password):
        serializer = AccountSerializer(account, many= False)   
        return Response(serializer.data) 
    else:
        return Response(status=404)
    