from django.contrib import admin
from .models import Ingredient,Type
# Register your models here.


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name','type','draft')
    search_fields = ['name']
    list_filter = ['type','draft']

admin.site.register(Ingredient,IngredientAdmin)
admin.site.register(Type)
