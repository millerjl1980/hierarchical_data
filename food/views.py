from django.shortcuts import render

from food.models import Food

# Create your views here.
def home(request):
    return render(request, 'home.html',
                  {'nodes': Food.objects.all()})