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


def remove_from_fieldsets(fieldsets, fields):
    for fieldset in fieldsets:
        for field in fields:
            if field in fieldset[1]['fields']:
                new_fields = []
                for new_field in fieldset[1]['fields']:
                    if not new_field in fields:
                        new_fields.append(new_field)
                        
                fieldset[1]['fields'] = tuple(new_fields)
                break

class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [StepInstanceInline,IngredientInstanceInline]
    list_filter = ['category','draft'] 
    list_display = ('name','category','draft') 

    def get_fieldsets(self, request, obj=None):
        fieldsets = super(RecipeAdmin, self).get_fieldsets(request, obj)
	
        if not request.user.is_superuser and request.user.groups.filter(name='publisher').count() == 0:
            remove_from_fieldsets(fieldsets, ('draft','slug',))
        return fieldsets

admin.site.register(Category)
admin.site.register(Recipe,RecipeAdmin)
