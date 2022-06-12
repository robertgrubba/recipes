from django import forms
from django.core.exceptions import ValidationError
from ingredients.models import Ingredient

class HoneypotField(forms.BooleanField):
    default_widget = forms.CheckboxInput(
        {"style": "display:none !important;", "tabindex": "-1", "autocomplete": "off"}
    )

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", HoneypotField.default_widget)
        kwargs["required"] = False
        super().__init__(*args, **kwargs)

    def clean(self, value):
        if cleaned_value := super().clean(value):
            raise ValidationError("")
        else:
            return cleaned_value

class CalcForm(forms.Form):
    accept_rules = HoneypotField(label=False)
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.filter(draft=False).all(),required=False)
    amount = forms.FloatField(required=False)
    MEASURE_UNITS = (
            ('g','gram'),
            ('oz','ounce'),
            ('ts','teaspoon'),
            ('tb','tablespoon'),
            ('cu','cup'),
            ('gl','glass'),
            ('ml','mililiters'),
            ('l','liter'),
            ('p','piece'),
            ('b','bunch'),
            ('s','slice'),
            ('c','clove'),
    )
    measure = forms.ChoiceField(choices = MEASURE_UNITS, required=False) 
