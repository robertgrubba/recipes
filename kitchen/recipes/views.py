from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from .models import Recipe,Category,Ingredient
from .forms import CalcForm
from ingredients.models import Ingredient as ING
import datetime

# Create your views here.


class RecipeListView(ListView):
    model = Recipe

    def get_queryset(self):
        new_context = Recipe.objects.filter(draft=False)
        return new_context


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
                if ingredient.product.calories: calories =calories + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.calories)
                if ingredient.product.weight: weight = weight + (ingredient.amount * ingredient.product.weight)
                if ingredient.product.carbohydrates: carbohydrates = carbohydrates + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.carbohydrates)
                if ingredient.product.water: water = water + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.water)
                if ingredient.product.sugar: sugar = sugar + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.sugar)
                if ingredient.product.dietaryfiber: fiber = fiber + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.dietaryfiber)
                if ingredient.product.fat: fat = fat + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.fat)
                if ingredient.product.protein: protein = protein + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.protein)
                if ingredient.product.vita: vita = vita + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vita)
                if ingredient.product.vita1: vita1 = vita1 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vita1)
                if ingredient.product.vitc: vitc = vitc + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitc)
                if ingredient.product.vitb1: vitb1 = vitb1 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb1)
                if ingredient.product.vitb2: vitb2 = vitb2 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb2)
                if ingredient.product.vitb3: vitb3 = vitb3 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb3)
                if ingredient.product.vitb5: vitb5 = vitb5 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb5)
                if ingredient.product.vitb6: vitb6 = vitb6 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb6)
                if ingredient.product.vitb9: vitb9 = vitb9 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb9)
                if ingredient.product.vitb12: vitb12 = vitb12 + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitb12)
                if ingredient.product.vite: vite = vite + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vite)
                if ingredient.product.vitk: vitk = vitk + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.vitk)
                if ingredient.product.calcium: calcium = calcium + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.calcium)
                if ingredient.product.copper: copper = copper + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.copper)
                if ingredient.product.iron: iron = iron + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.iron)
                if ingredient.product.magnesium: magnesium = magnesium + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.magnesium)
                if ingredient.product.manganese: manganese = manganese + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.manganese)
                if ingredient.product.phosphorous: phosphorous = phosphorous + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.phosphorous)
                if ingredient.product.potassium: potassium = potassium + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.potassium)
                if ingredient.product.selenium: selenium = selenium + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.selenium)
                if ingredient.product.sodium: sodium = sodium + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.sodium)
                if ingredient.product.zinc: zinc = zinc + ((ingredient.amount * ingredient.product.weight)/100 * ingredient.product.zinc)

            if ingredient.measure == 'cu': 
                if ingredient.product.calories: calories =calories + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.calories)
                if ingredient.product.cup: weight = weight + (ingredient.amount * ingredient.product.cup)
                if ingredient.product.carbohydrates: carbohydrates = carbohydrates + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.carbohydrates)
                if ingredient.product.water: water = water + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.water)
                if ingredient.product.sugar: sugar = sugar + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.sugar)
                if ingredient.product.dietaryfiber: fiber = fiber + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.dietaryfiber)
                if ingredient.product.fat: fat = fat + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.fat)
                if ingredient.product.protein: protein = protein + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.protein)
                if ingredient.product.vita: vita = vita + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vita)
                if ingredient.product.vita1: vita1 = vita1 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vita1)
                if ingredient.product.vitc: vitc = vitc + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitc)
                if ingredient.product.vitb1: vitb1 = vitb1 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb1)
                if ingredient.product.vitb2: vitb2 = vitb2 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb2)
                if ingredient.product.vitb3: vitb3 = vitb3 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb3)
                if ingredient.product.vitb5: vitb5 = vitb5 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb5)
                if ingredient.product.vitb6: vitb6 = vitb6 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb6)
                if ingredient.product.vitb9: vitb9 = vitb9 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb9)
                if ingredient.product.vitb12: vitb12 = vitb12 + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitb12)
                if ingredient.product.vite: vite = vite + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vite)
                if ingredient.product.vitk: vitk = vitk + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.vitk)
                if ingredient.product.calcium: calcium = calcium + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.calcium)
                if ingredient.product.copper: copper = copper + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.copper)
                if ingredient.product.iron: iron = iron + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.iron)
                if ingredient.product.magnesium: magnesium = magnesium + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.magnesium)
                if ingredient.product.manganese: manganese = manganese + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.manganese)
                if ingredient.product.phosphorous: phosphorous = phosphorous + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.phosphorous)
                if ingredient.product.potassium: potassium = potassium + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.potassium)
                if ingredient.product.selenium: selenium = selenium + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.selenium)
                if ingredient.product.sodium: sodium = sodium + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.sodium)
                if ingredient.product.zinc: zinc = zinc + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.zinc)

            if ingredient.measure == 'gl': 
                if ingredient.product.calories: calories =calories + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.calories)
                if ingredient.product.glass: weight = weight + (ingredient.amount * ingredient.product.glass)
                if ingredient.product.carbohydrates: carbohydrates = carbohydrates + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.carbohydrates)
                if ingredient.product.water: water = water + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.water)
                if ingredient.product.sugar: sugar = sugar + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.sugar)
                if ingredient.product.dietaryfiber: fiber = fiber + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.dietaryfiber)
                if ingredient.product.fat: fat = fat + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.fat)
                if ingredient.product.protein: protein = protein + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.protein)
                if ingredient.product.vita: vita = vita + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vita)
                if ingredient.product.vita1: vita1 = vita1 + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vita1)
                if ingredient.product.vitc: vitc = vitc + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vitc)
                if ingredient.product.vitb1: vitb1 = vitb1 + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vitb1)
                if ingredient.product.vitb2: vitb2 = vitb2 + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vitb2)
                if ingredient.product.vitb3: vitb3 = vitb3 + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vitb3)
                if ingredient.product.vitb5: vitb5 = vitb5 + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vitb5)
                if ingredient.product.vitb6: vitb6 = vitb6 + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vitb6)
                if ingredient.product.vitb9: vitb9 = vitb9 + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vitb9)
                if ingredient.product.vitb12: vitb12 = vitb12 + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vitb12)
                if ingredient.product.vite: vite = vite + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vite)
                if ingredient.product.vitk: vitk = vitk + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.vitk)
                if ingredient.product.calcium: calcium = calcium + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.calcium)
                if ingredient.product.copper: copper = copper + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.copper)
                if ingredient.product.iron: iron = iron + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.iron)
                if ingredient.product.magnesium: magnesium = magnesium + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.magnesium)
                if ingredient.product.manganese: manganese = manganese + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.manganese)
                if ingredient.product.phosphorous: phosphorous = phosphorous + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.phosphorous)
                if ingredient.product.potassium: potassium = potassium + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.potassium)
                if ingredient.product.selenium: selenium = selenium + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.selenium)
                if ingredient.product.sodium: sodium = sodium + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.sodium)
                if ingredient.product.zinc: zinc = zinc + ((ingredient.amount * ingredient.product.glass)/100 * ingredient.product.zinc)

            if ingredient.measure == 'b': 
                if ingredient.product.calories: calories =calories + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.calories)
                if ingredient.product.bunch: weight = weight + (ingredient.amount * ingredient.product.bunch)
                if ingredient.product.carbohydrates: carbohydrates = carbohydrates + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.carbohydrates)
                if ingredient.product.water: water = water + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.water)
                if ingredient.product.sugar: sugar = sugar + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.sugar)
                if ingredient.product.dietaryfiber: fiber = fiber + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.dietaryfiber)
                if ingredient.product.fat: fat = fat + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.fat)
                if ingredient.product.protein: protein = protein + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.protein)
                if ingredient.product.vita: vita = vita + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vita)
                if ingredient.product.vita1: vita1 = vita1 + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vita1)
                if ingredient.product.vitc: vitc = vitc + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vitc)
                if ingredient.product.vitb1: vitb1 = vitb1 + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vitb1)
                if ingredient.product.vitb2: vitb2 = vitb2 + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vitb2)
                if ingredient.product.vitb3: vitb3 = vitb3 + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vitb3)
                if ingredient.product.vitb5: vitb5 = vitb5 + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vitb5)
                if ingredient.product.vitb6: vitb6 = vitb6 + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vitb6)
                if ingredient.product.vitb9: vitb9 = vitb9 + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vitb9)
                if ingredient.product.vitb12: vitb12 = vitb12 + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vitb12)
                if ingredient.product.vite: vite = vite + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vite)
                if ingredient.product.vitk: vitk = vitk + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.vitk)
                if ingredient.product.calcium: calcium = calcium + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.calcium)
                if ingredient.product.copper: copper = copper + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.copper)
                if ingredient.product.iron: iron = iron + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.iron)
                if ingredient.product.magnesium: magnesium = magnesium + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.magnesium)
                if ingredient.product.manganese: manganese = manganese + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.manganese)
                if ingredient.product.phosphorous: phosphorous = phosphorous + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.phosphorous)
                if ingredient.product.potassium: potassium = potassium + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.potassium)
                if ingredient.product.selenium: selenium = selenium + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.selenium)
                if ingredient.product.sodium: sodium = sodium + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.sodium)
                if ingredient.product.zinc: zinc = zinc + ((ingredient.amount * ingredient.product.bunch)/100 * ingredient.product.zinc)

            if ingredient.measure == 's': 
                if ingredient.product.calories: calories =calories + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.calories)
                if ingredient.product.slice: weight = weight + (ingredient.amount * ingredient.product.slice)
                if ingredient.product.carbohydrates: carbohydrates = carbohydrates + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.carbohydrates)
                if ingredient.product.water: water = water + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.water)
                if ingredient.product.sugar: sugar = sugar + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.sugar)
                if ingredient.product.dietaryfiber: fiber = fiber + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.dietaryfiber)
                if ingredient.product.fat: fat = fat + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.fat)
                if ingredient.product.protein: protein = protein + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.protein)
                if ingredient.product.vita: vita = vita + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vita)
                if ingredient.product.vita1: vita1 = vita1 + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vita1)
                if ingredient.product.vitc: vitc = vitc + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vitc)
                if ingredient.product.vitb1: vitb1 = vitb1 + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vitb1)
                if ingredient.product.vitb2: vitb2 = vitb2 + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vitb2)
                if ingredient.product.vitb3: vitb3 = vitb3 + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vitb3)
                if ingredient.product.vitb5: vitb5 = vitb5 + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vitb5)
                if ingredient.product.vitb6: vitb6 = vitb6 + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vitb6)
                if ingredient.product.vitb9: vitb9 = vitb9 + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vitb9)
                if ingredient.product.vitb12: vitb12 = vitb12 + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vitb12)
                if ingredient.product.vite: vite = vite + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vite)
                if ingredient.product.vitk: vitk = vitk + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.vitk)
                if ingredient.product.calcium: calcium = calcium + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.calcium)
                if ingredient.product.copper: copper = copper + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.copper)
                if ingredient.product.iron: iron = iron + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.iron)
                if ingredient.product.magnesium: magnesium = magnesium + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.magnesium)
                if ingredient.product.manganese: manganese = manganese + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.manganese)
                if ingredient.product.phosphorous: phosphorous = phosphorous + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.phosphorous)
                if ingredient.product.potassium: potassium = potassium + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.potassium)
                if ingredient.product.selenium: selenium = selenium + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.selenium)
                if ingredient.product.sodium: sodium = sodium + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.sodium)
                if ingredient.product.zinc: zinc = zinc + ((ingredient.amount * ingredient.product.slice)/100 * ingredient.product.zinc)

            if ingredient.measure == 'c': 
                if ingredient.product.calories: calories =calories + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.calories)
                if ingredient.product.clove: weight = weight + (ingredient.amount * ingredient.product.clove)
                if ingredient.product.carbohydrates: carbohydrates = carbohydrates + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.carbohydrates)
                if ingredient.product.water: water = water + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.water)
                if ingredient.product.sugar: sugar = sugar + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.sugar)
                if ingredient.product.dietaryfiber: fiber = fiber + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.dietaryfiber)
                if ingredient.product.fat: fat = fat + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.fat)
                if ingredient.product.protein: protein = protein + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.protein)
                if ingredient.product.vita: vita = vita + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vita)
                if ingredient.product.vita1: vita1 = vita1 + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vita1)
                if ingredient.product.vitc: vitc = vitc + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vitc)
                if ingredient.product.vitb1: vitb1 = vitb1 + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vitb1)
                if ingredient.product.vitb2: vitb2 = vitb2 + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vitb2)
                if ingredient.product.vitb3: vitb3 = vitb3 + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vitb3)
                if ingredient.product.vitb5: vitb5 = vitb5 + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vitb5)
                if ingredient.product.vitb6: vitb6 = vitb6 + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vitb6)
                if ingredient.product.vitb9: vitb9 = vitb9 + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vitb9)
                if ingredient.product.vitb12: vitb12 = vitb12 + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vitb12)
                if ingredient.product.vite: vite = vite + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vite)
                if ingredient.product.vitk: vitk = vitk + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.vitk)
                if ingredient.product.calcium: calcium = calcium + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.calcium)
                if ingredient.product.copper: copper = copper + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.copper)
                if ingredient.product.iron: iron = iron + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.iron)
                if ingredient.product.magnesium: magnesium = magnesium + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.magnesium)
                if ingredient.product.manganese: manganese = manganese + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.manganese)
                if ingredient.product.phosphorous: phosphorous = phosphorous + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.phosphorous)
                if ingredient.product.potassium: potassium = potassium + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.potassium)
                if ingredient.product.selenium: selenium = selenium + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.selenium)
                if ingredient.product.sodium: sodium = sodium + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.sodium)
                if ingredient.product.zinc: zinc = zinc + ((ingredient.amount * ingredient.product.clove)/100 * ingredient.product.zinc)

            if ingredient.measure == 'ml': 
                if ingredient.product.calories: calories =calories + ((ingredient.amount )/100 * ingredient.product.calories)
                weight = weight + (ingredient.amount )
                if ingredient.product.carbohydrates: carbohydrates = carbohydrates + ((ingredient.amount )/100 * ingredient.product.carbohydrates)
                if ingredient.product.water: water = water + ((ingredient.amount )/100 * ingredient.product.water)
                if ingredient.product.sugar: sugar = sugar + ((ingredient.amount )/100 * ingredient.product.sugar)
                if ingredient.product.dietaryfiber: fiber = fiber + ((ingredient.amount )/100 * ingredient.product.dietaryfiber)
                if ingredient.product.fat: fat = fat + ((ingredient.amount )/100 * ingredient.product.fat)
                if ingredient.product.protein: protein = protein + ((ingredient.amount )/100 * ingredient.product.protein)
                if ingredient.product.vita: vita = vita + ((ingredient.amount )/100 * ingredient.product.vita)
                if ingredient.product.vita1: vita1 = vita1 + ((ingredient.amount )/100 * ingredient.product.vita1)
                if ingredient.product.vitc: vitc = vitc + ((ingredient.amount )/100 * ingredient.product.vitc)
                if ingredient.product.vitb1: vitb1 = vitb1 + ((ingredient.amount )/100 * ingredient.product.vitb1)
                if ingredient.product.vitb2: vitb2 = vitb2 + ((ingredient.amount )/100 * ingredient.product.vitb2)
                if ingredient.product.vitb3: vitb3 = vitb3 + ((ingredient.amount )/100 * ingredient.product.vitb3)
                if ingredient.product.vitb5: vitb5 = vitb5 + ((ingredient.amount )/100 * ingredient.product.vitb5)
                if ingredient.product.vitb6: vitb6 = vitb6 + ((ingredient.amount )/100 * ingredient.product.vitb6)
                if ingredient.product.vitb9: vitb9 = vitb9 + ((ingredient.amount )/100 * ingredient.product.vitb9)
                if ingredient.product.vitb12: vitb12 = vitb12 + ((ingredient.amount )/100 * ingredient.product.vitb12)
                if ingredient.product.vite: vite = vite + ((ingredient.amount )/100 * ingredient.product.vite)
                if ingredient.product.vitk: vitk = vitk + ((ingredient.amount )/100 * ingredient.product.vitk)
                if ingredient.product.calcium: calcium = calcium + ((ingredient.amount )/100 * ingredient.product.calcium)
                if ingredient.product.copper: copper = copper + ((ingredient.amount )/100 * ingredient.product.copper)
                if ingredient.product.iron: iron = iron + ((ingredient.amount )/100 * ingredient.product.iron)
                if ingredient.product.magnesium: magnesium = magnesium + ((ingredient.amount )/100 * ingredient.product.magnesium)
                if ingredient.product.manganese: manganese = manganese + ((ingredient.amount )/100 * ingredient.product.manganese)
                if ingredient.product.phosphorous: phosphorous = phosphorous + ((ingredient.amount )/100 * ingredient.product.phosphorous)
                if ingredient.product.potassium: potassium = potassium + ((ingredient.amount )/100 * ingredient.product.potassium)
                if ingredient.product.selenium: selenium = selenium + ((ingredient.amount )/100 * ingredient.product.selenium)
                if ingredient.product.sodium: sodium = sodium + ((ingredient.amount )/100 * ingredient.product.sodium)
                if ingredient.product.zinc: zinc = zinc + ((ingredient.amount )/100 * ingredient.product.zinc)

            if ingredient.measure == 'l': 
                if ingredient.product.calories: calories =calories + ((ingredient.amount * 1000 )/100 * ingredient.product.calories)
                weight = weight + (ingredient.amount * 1000 )
                if ingredient.product.carbohydrates: carbohydrates = carbohydrates + ((ingredient.amount * 1000 )/100 * ingredient.product.carbohydrates)
                if ingredient.product.water: water = water + ((ingredient.amount * 1000 )/100 * ingredient.product.water)
                if ingredient.product.sugar: sugar = sugar + ((ingredient.amount * 1000 )/100 * ingredient.product.sugar)
                if ingredient.product.dietaryfiber: fiber = fiber + ((ingredient.amount * 1000 )/100 * ingredient.product.dietaryfiber)
                if ingredient.product.fat: fat = fat + ((ingredient.amount * 1000 )/100 * ingredient.product.fat)
                if ingredient.product.protein: protein = protein + ((ingredient.amount * 1000 )/100 * ingredient.product.protein)
                if ingredient.product.vita: vita = vita + ((ingredient.amount * 1000 )/100 * ingredient.product.vita)
                if ingredient.product.vita1: vita1 = vita1 + ((ingredient.amount * 1000 )/100 * ingredient.product.vita1)
                if ingredient.product.vitc: vitc = vitc + ((ingredient.amount * 1000 )/100 * ingredient.product.vitc)
                if ingredient.product.vitb1: vitb1 = vitb1 + ((ingredient.amount * 1000 )/100 * ingredient.product.vitb1)
                if ingredient.product.vitb2: vitb2 = vitb2 + ((ingredient.amount * 1000 )/100 * ingredient.product.vitb2)
                if ingredient.product.vitb3: vitb3 = vitb3 + ((ingredient.amount * 1000 )/100 * ingredient.product.vitb3)
                if ingredient.product.vitb5: vitb5 = vitb5 + ((ingredient.amount * 1000 )/100 * ingredient.product.vitb5)
                if ingredient.product.vitb6: vitb6 = vitb6 + ((ingredient.amount * 1000 )/100 * ingredient.product.vitb6)
                if ingredient.product.vitb9: vitb9 = vitb9 + ((ingredient.amount * 1000 )/100 * ingredient.product.vitb9)
                if ingredient.product.vitb12: vitb12 = vitb12 + ((ingredient.amount * 1000 )/100 * ingredient.product.vitb12)
                if ingredient.product.vite: vite = vite + ((ingredient.amount * 1000 )/100 * ingredient.product.vite)
                if ingredient.product.vitk: vitk = vitk + ((ingredient.amount * 1000 )/100 * ingredient.product.vitk)
                if ingredient.product.calcium: calcium = calcium + ((ingredient.amount * 1000 )/100 * ingredient.product.calcium)
                if ingredient.product.copper: copper = copper + ((ingredient.amount * 1000 )/100 * ingredient.product.copper)
                if ingredient.product.iron: iron = iron + ((ingredient.amount * 1000 )/100 * ingredient.product.iron)
                if ingredient.product.magnesium: magnesium = magnesium + ((ingredient.amount * 1000 )/100 * ingredient.product.magnesium)
                if ingredient.product.manganese: manganese = manganese + ((ingredient.amount * 1000 )/100 * ingredient.product.manganese)
                if ingredient.product.phosphorous: phosphorous = phosphorous + ((ingredient.amount * 1000 )/100 * ingredient.product.phosphorous)
                if ingredient.product.potassium: potassium = potassium + ((ingredient.amount * 1000 )/100 * ingredient.product.potassium)
                if ingredient.product.selenium: selenium = selenium + ((ingredient.amount * 1000 )/100 * ingredient.product.selenium)
                if ingredient.product.sodium: sodium = sodium + ((ingredient.amount * 1000 )/100 * ingredient.product.sodium)
                if ingredient.product.zinc: zinc = zinc + ((ingredient.amount * 1000 )/100 * ingredient.product.zinc)

            if ingredient.measure == 'g': 
                if ingredient.product.calories: calories =calories + ((ingredient.amount )/100 * ingredient.product.calories)
                weight = weight + (ingredient.amount )
                if ingredient.product.carbohydrates: carbohydrates = carbohydrates + ((ingredient.amount )/100 * ingredient.product.carbohydrates)
                if ingredient.product.water: water = water + ((ingredient.amount )/100 * ingredient.product.water)
                if ingredient.product.sugar: sugar = sugar + ((ingredient.amount )/100 * ingredient.product.sugar)
                if ingredient.product.dietaryfiber: fiber = fiber + ((ingredient.amount )/100 * ingredient.product.dietaryfiber)
                if ingredient.product.fat: fat = fat + ((ingredient.amount )/100 * ingredient.product.fat)
                if ingredient.product.protein: protein = protein + ((ingredient.amount )/100 * ingredient.product.protein)
                if ingredient.product.vita: vita = vita + ((ingredient.amount )/100 * ingredient.product.vita)
                if ingredient.product.vita1: vita1 = vita1 + ((ingredient.amount )/100 * ingredient.product.vita1)
                if ingredient.product.vitc: vitc = vitc + ((ingredient.amount )/100 * ingredient.product.vitc)
                if ingredient.product.vitb1: vitb1 = vitb1 + ((ingredient.amount )/100 * ingredient.product.vitb1)
                if ingredient.product.vitb2: vitb2 = vitb2 + ((ingredient.amount )/100 * ingredient.product.vitb2)
                if ingredient.product.vitb3: vitb3 = vitb3 + ((ingredient.amount )/100 * ingredient.product.vitb3)
                if ingredient.product.vitb5: vitb5 = vitb5 + ((ingredient.amount )/100 * ingredient.product.vitb5)
                if ingredient.product.vitb6: vitb6 = vitb6 + ((ingredient.amount )/100 * ingredient.product.vitb6)
                if ingredient.product.vitb9: vitb9 = vitb9 + ((ingredient.amount )/100 * ingredient.product.vitb9)
                if ingredient.product.vitb12: vitb12 = vitb12 + ((ingredient.amount )/100 * ingredient.product.vitb12)
                if ingredient.product.vite: vite = vite + ((ingredient.amount )/100 * ingredient.product.vite)
                if ingredient.product.vitk: vitk = vitk + ((ingredient.amount )/100 * ingredient.product.vitk)
                if ingredient.product.calcium: calcium = calcium + ((ingredient.amount )/100 * ingredient.product.calcium)
                if ingredient.product.copper: copper = copper + ((ingredient.amount )/100 * ingredient.product.copper)
                if ingredient.product.iron: iron = iron + ((ingredient.amount )/100 * ingredient.product.iron)
                if ingredient.product.magnesium: magnesium = magnesium + ((ingredient.amount )/100 * ingredient.product.magnesium)
                if ingredient.product.manganese: manganese = manganese + ((ingredient.amount )/100 * ingredient.product.manganese)
                if ingredient.product.phosphorous: phosphorous = phosphorous + ((ingredient.amount )/100 * ingredient.product.phosphorous)
                if ingredient.product.potassium: potassium = potassium + ((ingredient.amount )/100 * ingredient.product.potassium)
                if ingredient.product.selenium: selenium = selenium + ((ingredient.amount )/100 * ingredient.product.selenium)
                if ingredient.product.sodium: sodium = sodium + ((ingredient.amount )/100 * ingredient.product.sodium)
                if ingredient.product.zinc: zinc = zinc + ((ingredient.amount )/100 * ingredient.product.zinc)

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

def calc(request):
    verified = ING.objects.filter(draft=False).count()
    if request.method == 'POST':
        form = CalcForm(request.POST)
        ok = True
        if not 'saved' in request.session or not request.session['saved']:
            request.session['saved']=[]
        else:
            saved_list = request.session['saved']

        if form.is_valid():
            if not 'finish' in request.session:
                if form.cleaned_data['ingredient'] == None or form.cleaned_data['amount'] == None:
                    ok = False
            if ok:
                if not 'saved' in request.session or not request.session['saved']:
                    ingredient = {
                            "id": form.cleaned_data['ingredient'].id,
                            "name": form.cleaned_data['ingredient'].name,
                            "amount": form.cleaned_data['amount'],
                            "measure": form.cleaned_data['measure'],
                            }
                    request.session['saved']=[ingredient,]
                    saved_list = request.session['saved']
                else:
                    saved_list = request.session['saved']
                    if 'add_ingredient' in request.POST:
                        ingredient = {
                                "id": form.cleaned_data['ingredient'].id,
                                "name": form.cleaned_data['ingredient'].name,
                                "amount": form.cleaned_data['amount'],
                                "measure": form.cleaned_data['measure'],
                                }
                        saved_list.append(ingredient)
                        print(ingredient)
                    request.session['saved']=saved_list

                form = CalcForm()
            else:
                if 'finish' in request.POST and len(saved_list)>0:
                    now = datetime.datetime.now()
                    temp_recipe = Recipe(
                            name="temporary recipe "+str(now)+" ",
                            category = None,
                            serves = 4,
                            time = 10,
                            description = "recipe from recipe calculator")
                    temp_recipe.save()
                    for ingredient in request.session['saved']:
                        new_ingredient = Ingredient(product=ING.objects.get(pk=int(ingredient['id'])), amount=ingredient['amount'], measure=ingredient['measure'])
                        new_ingredient.save()
                        temp_recipe.ingredients.add(new_ingredient)
                        temp_recipe.save()

                    temp_recipe.save()
                    saved_list = None
                    request.session['saved'] = None
                    request.session.modified = True
                    return redirect(temp_recipe)

                if 'remove_ingredient' in request.POST and len(saved_list)>0:
                    saved_list.pop()
                    request.session['saved']=saved_list
                
                if 'rmrf' in request.POST:
                    saved_list = None
                    request.session['saved'] = None
                    request.session.modified = True

                saved_list=request.session['saved']
    else:
        form = CalcForm()
        if not 'saved' in request.session or not request.session['saved']:
            saved_list = None
        else:
            saved_list = request.session['saved']


    context = {
            'verified':verified,
            'form':form,
            'saved_list':saved_list,
            }

    return render(request, 'recipes/calc_form.html',context)
