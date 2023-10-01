from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home ,name="home"),
    path('rooms/<str:pk>/', views.room ,name="room"),
    path('create-rooms/', views.create_room ,name="create-room"),
    path('update-rooms/<str:pk>/', views.update_room ,name="update-room"),
    path('delete-rooms/<str:pk>/', views.delete_room ,name="delete-room"),
]
