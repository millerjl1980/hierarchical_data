from django.urls import path

from food import views

urlpatterns = [
    path('', views.home, name='home'),
]