from django.urls import path
from . import views

urlpatterns = [
    path('clothes/<str:id>/', views.getClothe, name="clothe"),
    path('clothes/', views.getClothes, name="clothes"),
]
