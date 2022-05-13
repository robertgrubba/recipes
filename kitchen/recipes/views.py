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
            if ingredient.measure == 'cu': 
                calories =calories + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.calories)
                weight = weight + (ingredient.amount * ingredient.product.cup)
                carbohydrates = carbohydrates + (ingredient.amount * ingredient.product.cup)/100 * ingredient.product.carbohydrates
                water = water + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.water)
                sugar = sugar + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.sugar)
                fiber = fiber + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.dietaryfiber)
                fat = fat + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.fat)
                protein = protein + ((ingredient.amount * ingredient.product.cup)/100 * ingredient.product.protein)


        context['calories']=round(calories,2)
        context['weight']=round(weight,2)
        context['carbohydrates']=round(carbohydrates,2)
        context['water']=round(water,2)
        context['sugar']=round(sugar,2)
        context['fiber']=round(fiber,2)
        context['fat']=round(fat,2)
        context['protein']=round(protein,2)

        return context

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category
