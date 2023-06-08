from django.urls import path
from . import views

urlpatterns = [
   path('comments/create/', views.create_comment, name="createComment"),
   path('comments/<str:itemType>/<str:product_id>', views.get_all_comments, name="comments"),
]
