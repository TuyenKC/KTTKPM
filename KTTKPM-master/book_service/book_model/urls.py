from django.urls import path
from . import views

urlpatterns = [
    path('books/<str:id>/', views.getBook, name="book"),
    path('books/', views.getBooks, name="books"),
]
