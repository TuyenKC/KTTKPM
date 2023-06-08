from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('cart/<str:id>', views.getCart, name="cart"),
    path('cart/update/<str:account_id>/<str:cart_item_id>', views.update_cart_item_quantity, name="updateCart"),
    path('cart/clear/<str:account_id>/', views.clearCart, name="clearCart"),
    path('cart/create/', views.createCart, name="createCart"),
    path('cart/remove/<str:account_id>/<str:cart_item_id>/', views.removeItemCart, name="removeItemCart"),
    path('cart/add/<str:account_id>/', views.add_item_to_cart, name="addItemCart")
]
