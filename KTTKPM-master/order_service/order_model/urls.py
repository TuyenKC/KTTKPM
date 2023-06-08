from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('order/<str:account_id>', views.getOrders, name="order"),
    path('order/create/', views.createOrder, name="createOrder"),
]
