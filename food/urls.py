from django.urls import path

from food import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generic_form.html', views.add_food, name='addfood'),
]