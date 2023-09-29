from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home ,name="home"),
    path('rooms/<str:pk>/', views.room ,name="room"),
]
