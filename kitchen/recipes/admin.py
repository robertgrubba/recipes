from django.contrib import admin
from .models import Ingredient,Category,Recipe,Step

class CategoryInstanceInline(admin.TabularInline):
    model = Category
    extra = 1

class StepInstanceInline(admin.TabularInline):
    model = Step
    extra = 1

class IngredientInstanceInline(admin.TabularInline):
    model = Ingredient
    extra = 1

class RecipeInstanceInline(admin.TabularInline):
    model = Recipe
    extra = 1

#class PersonAdmin(admin.ModelAdmin):
#        list_display = ('name','surname','nickname')
#        list_filter = ('places__city__name',)
#        search_fields = ['name','surname','nickname']
#        inlines = [PlaceInstanceInline,TelephoneInstanceInline,VehicleInstanceInline,WebpageInstanceInline,FileInstanceInline,NoteInstanceInline]

class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [StepInstanceInline,IngredientInstanceInline]
    list_filter = ['category','draft'] 
    list_display = ('name','category','draft') 

admin.site.register(Category)
admin.site.register(Recipe,RecipeAdmin)
