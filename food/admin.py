from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from food.models import Food

# Register your models here.

admin.site.register(Food, DraggableMPTTAdmin)
