from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Ingredient

# Create your views here.

def index(request):
    return render(request, 'index.html')

class IngredientListView(ListView):
        model = Ingredient

