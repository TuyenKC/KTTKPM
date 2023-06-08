from django.urls import path
from . import views

urlpatterns = [
    path('shoes/<str:id>/', views.getShoe, name="shoe"),
    path('shoes/', views.getShoes, name="shoes"),
]
