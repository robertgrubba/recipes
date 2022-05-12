from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Recipe
# Create your views here.


class RecipeListView(ListView):
    model = Recipe

class RecipeDetailView(DetailView):
    model = Recipe

