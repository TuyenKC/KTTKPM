from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('accounts/login', views.loginAccount, name="loginAccount"),
    path('accounts/create', views.createAccount, name="createAccount"),
    path('accounts/<str:id>', views.getAccount, name="account"),
    path('accounts/', views.getAccounts, name="accounts"),
]
