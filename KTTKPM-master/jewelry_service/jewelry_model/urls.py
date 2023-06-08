from django.urls import path
from . import views

urlpatterns = [
    path('jewelrys/<str:id>/', views.getJewelry, name="jewelry"),
    path('jewelrys/', views.getJewelrys, name="jewelrys"),
]
