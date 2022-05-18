import json
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .models import Ingredient

# Create your views here.

def index(request):
    return render(request, 'index.html')

def load(request):
    f=open('static/assets/food.json')
    data=json.load(f)

    for i in data:
        if Ingredient.objects.filter(ndbn=str(i['Nutrient Data Bank Number'])).exists():
            pass
        else:
            new_object = Ingredient(
                    name = i['Description'],
                    ndbn = i['Nutrient Data Bank Number'],
                    alphacarotene = float(i['Data']['Alpha Carotene'])/1000,
                    betacarotene = float(i['Data']['Beta Carotene'])/1000,
                    betacryptoxanthin = float(i['Data']['Beta Cryptoxanthin'])/1000,
                    carbohydrates = float(i['Data']['Carbohydrate']),
                    cholesterol = float(i['Data']['Cholesterol']),
                    choline = float(i['Data']['Choline']),
                    dietaryfiber = float(i['Data']['Fiber']),
                    luteinzeaxanthin = float(i['Data']['Lutein and Zeaxanthin'])/1000,
                    lycopene = float(i['Data']['Lycopene'])/1000,
                    vitb3 = float(i['Data']['Niacin']),
                    protein = float(i['Data']['Protein']),
                    vita1 = float(i['Data']['Retinol'])/1000,
                    vitb2 = float(i['Data']['Riboflavin']),
                    selenium = float(i['Data']['Selenium']),
                    sugar = float(i['Data']['Sugar Total']),
                    vitb1 = float(i['Data']['Thiamin']),
                    water = int(i['Data']['Water']),
                    monosaturatedfat = float(i['Data']['Fat']['Monosaturated Fat']),
                    polysaturatedfat = float(i['Data']['Fat']['Polysaturated Fat']),
                    saturatedfat = float(i['Data']['Fat']['Saturated Fat']),
                    fat = float(i['Data']['Fat']['Total Lipid']),
                    calcium = int(i['Data']['Major Minerals']['Calcium']),
                    copper = float(i['Data']['Major Minerals']['Copper']),
                    iron = float(i['Data']['Major Minerals']['Iron']),
                    magnesium = float(i['Data']['Major Minerals']['Magnesium']),
                    phosphorous = int(i['Data']['Major Minerals']['Phosphorus']),
                    potassium = float(i['Data']['Major Minerals']['Potassium']),
                    sodium = float(i['Data']['Major Minerals']['Sodium']),
                    zinc = float(i['Data']['Major Minerals']['Zinc']),
                    vita = float(i['Data']['Vitamins']['Vitamin A - RAE'])/1000,
                    vitb12 = float(i['Data']['Vitamins']['Vitamin B12'])/1000,
                    vitb6 = float(i['Data']['Vitamins']['Vitamin B6']),
                    vitc = float(i['Data']['Vitamins']['Vitamin C']),
                    vite = float(i['Data']['Vitamins']['Vitamin E']),
                    vitk = float(i['Data']['Vitamins']['Vitamin K'])/1000
                    )
            new_object.save()
    f.close()

    return render(request,'index.html')

class IngredientListView(ListView):
    model = Ingredient

    def get_queryset(self):
        new_context = Ingredient.objects.filter(draft=False)
        return new_context

class IngredientDetailView(DetailView):
    model = Ingredient
