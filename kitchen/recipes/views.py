from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Recipe,Category
# Create your views here.


class RecipeListView(ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calories = 0
        weight = 0
        carbohydrates = 0
        water = 0
        sugar = 0
        fat = 0
        fiber = 0
        protein = 0

        vita  = 0
        vita1  = 0
        vitc  = 0
        vitb1  = 0
        vitb2  = 0
        vitb3  = 0
        vitb5  = 0
        vitb6  = 0
        vitb9  = 0
        vitb12  = 0
        vite  = 0
        vitk  = 0
        calcium  = 0
        copper  = 0
        iron  = 0
        magnesium  = 0
        manganese  = 0
        phosphorous  = 0
        potassium  = 0
        selenium  = 0
        sodium  = 0
        zinc  = 0
        for ingredient in context['recipe'].ingredients.all():
            if ingredient.measure == 'p':
                calories =calories + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.calories)
                weight = weight + (ingredient.amount * ingredient.product.weight)
                carbohydrates = carbohydrates + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.carbohydrates)
                water = water + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.water)
                sugar = sugar + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.sugar)
                fiber = fiber + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.dietaryfiber)
                fat = fat + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.fat)
                protein = protein + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.protein)
                vita = vita + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vita)
                vita1 = vita1 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vita1)
                vitc = vitc + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitc)
                vitb1 = vitb1 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb1)
                vitb2 = vitb2 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb2)
                vitb3 = vitb3 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb3)
                vitb5 = vitb5 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb5)
                vitb6 = vitb6 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb6)
                vitb9 = vitb9 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb9)
                vitb12 = vitb12 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb12)
                vite = vite + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vite)
                vitk = vitk + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitk)
                calcium = calcium + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.calcium)
                copper = copper + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.copper)
                iron = iron + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.iron)
                magnesium = magnesium + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.magnesium)
                manganese = manganese + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.manganese)
                phosphorous = phosphorous + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.phosphorous)
                potassium = potassium + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.potassium)
                selenium = selenium + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.selenium)
                sodium = sodium + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.sodium)
                zinc = zinc + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.zinc)
            if ingredient.measure == 'cu': 
                calories =calories + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.calories)
                weight = weight + (ingredient.amount * ingredient.product.cup)
                carbohydrates = carbohydrates + (ingredient.amount * ingredient.product.cup)/100 * ingredient.product.carbohydrates
                water = water + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.water)
                sugar = sugar + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.sugar)
                fiber = fiber + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.dietaryfiber)
                fat = fat + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.fat)
                protein = protein + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.protein)
                vita = vita + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vita)
                vita1 = vita1 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vita1)
                vitc = vitc + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitc)
                vitb1 = vitb1 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb1)
                vitb2 = vitb2 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb2)
                vitb3 = vitb3 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb3)
                vitb5 = vitb5 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb5)
                vitb6 = vitb6 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb6)
                vitb9 = vitb9 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb9)
                vitb12 = vitb12 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb12)
                vite = vite + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vite)
                vitk = vitk + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitk)
                calcium = calcium + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.calcium)
                copper = copper + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.copper)
                iron = iron + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.iron)
                magnesium = magnesium + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.magnesium)
                manganese = manganese + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.manganese)
                phosphorous = phosphorous + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.phosphorous)
                potassium = potassium + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.potassium)
                selenium = selenium + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.selenium)
                sodium = sodium + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.sodium)
                zinc = zinc + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.zinc)


        context['calories']=round(calories,2)
        context['weight']=round(weight,2)
        context['carbohydrates']=round(carbohydrates,2)
        context['water']=round(water,2)
        context['sugar']=round(sugar,2)
        context['fiber']=round(fiber,2)
        context['fat']=round(fat,2)
        context['protein']=round(protein,2)
        context['vita']=round(vita,2)
        context['vita1']=round(vita1,2)
        context['vitc']=round(vitc,2)
        context['vitb1']=round(vitb1,2)
        context['vitb2']=round(vitb2,2)
        context['vitb3']=round(vitb3,2)
        context['vitb5']=round(vitb5,2)
        context['vitb6']=round(vitb6,2)
        context['vitb9']=round(vitb9,2)
        context['vitb12']=round(vitb12,2)
        context['vite']=round(vite,2)
        context['vitk']=round(vitk,2)
        context['calcium']=round(calcium,2)
        context['copper']=round(copper,2)
        context['iron']=round(iron,2)
        context['magnesium']=round(magnesium,2)
        context['manganese']=round(manganese,2)
        context['phosphorous']=round(phosphorous,2)
        context['potassium']=round(potassium,2)
        context['selenium']=round(selenium,2)
        context['sodium']=round(sodium,2)
        context['zinc']=round(zinc,2)

        return context

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category
