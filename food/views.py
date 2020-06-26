from django.shortcuts import render, redirect

from food.models import Food
from food.forms import AddFoodForm

# Create your views here.
def home(request):
    return render(request, 'home.html',
                  {'nodes': Food.objects.all()})

def add_food(request):
    if request.method == 'POST':
        form = AddFoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddFoodForm()
    return render(request, 'generic_form.html', {'form': form})