from django.forms import modelform_factory

from food.models import Food

AddFoodForm = modelform_factory(Food, exclude=[])