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


@api_view(['GET'])
def getCart(request, id):
    cart = Cart.objects.get(account = id)
    serializer = CartSerializer(cart, many= False)
    cart_data = dict(serializer.data)
    items = cart_data["items"]
    for i in range(len(items)):
        url = items[i]["itemURL"]
        response = requests.get(url).json()
        cart_data["items"][i]["item"] = response
    return Response(cart_data)

@api_view(['POST'])
def update_cart_item_quantity(request, account_id, cart_item_id):
    cart = get_object_or_404(Cart, account=account_id)
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart=cart)

    quantity = request.data.get('quantity')
    if quantity is not None:
        cart_item.quantity = quantity
        cart_item.save()

    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)

 
@api_view(['GET'])   
def clearCart(request, account_id):
    cart = get_object_or_404(Cart, account = account_id)
    cart.items.all().delete()
    cart.save()  # Save the updated cart
    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)


 
@api_view(['POST'])
def createCart(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        cart = serializer.save()
        return Response({"detail": "Cart created successfully", "cart_id": cart.id}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def removeItemCart(request, account_id, cart_item_id):
    cart = get_object_or_404(Cart, id=account_id)
    cart_item = get_object_or_404(CartItem, id=cart_item_id, cart=cart)
    cart_item.delete()
    cart.save()
    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_item_to_cart(request, account_id):
    cart = get_object_or_404(Cart, account = account_id)
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')
    itemType = request.data.get('itemType')

    # Check if the item already exists in the cart
    existing_item = CartItem.objects.filter(
        cart=cart, product_id=product_id, itemType=itemType).first()

    if existing_item:
        existing_item.quantity += quantity
        existing_item.save()
    else:
        new_item = CartItem(cart=cart, product_id=product_id,
                            quantity=quantity, itemType=itemType)
        new_item.save()

    cart.save()
    serializer = CartSerializer(cart, many=False)
    return Response(serializer.data)