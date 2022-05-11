import datetime
from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse
#from ingredients.models import Ingredient

# Create your models here.

class Step(models.Model):
    description = models.TextField()
    recipe = models.ForeignKey('Recipe',on_delete=models.SET_NULL,null=True,related_name='steps')
    image = ResizedImageField(size=[500,300],quality=85,keep_meta=True,upload_to='images/%Y/%m/%d/',default=None,null=True,blank=True)

    def __str__(self):
        return self.recipe.name+" "+str(self.id)

class Ingredient(models.Model):
    product = models.ForeignKey('ingredients.Ingredient',on_delete=models.SET_NULL,null=True,related_name='ingredients')
    amount = models.FloatField()
    recipe = models.ForeignKey('Recipe',on_delete=models.SET_NULL,null=True)

    MEASURE_UNITS = (
            ('g','grams'),
            ('oz','ounces'),
            ('ts','teaspoons'),
            ('tb','tablespoons'),
            ('cu','cups'),
            ('ml','mililiters'),
            ('l','liters'),
            ('p','pieces'),
    )

    measure = models.CharField(max_length=2, choices=MEASURE_UNITS, blank=True, default='g',help_text="Measure units")

    def __str__(self):
        return self.recipe.name+" "+str(self.id)

class Category(models.Model):
    name = models.CharField(max_length=100, help_text='Category name')
    description = models.TextField()
    image = ResizedImageField(size=[500,300],quality=85,keep_meta=True,upload_to='images/%Y/%m/%d/',default=None,null=True,blank=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=200, help_text='Recipe name')
    description = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True,related_name='recipes')
    image = ResizedImageField(size=[500,300],quality=85,keep_meta=True,upload_to='images/%Y/%m/%d/',default=None,null=True,blank=True)
    time = models.IntegerField(help_text='Time required to prepare in minutes',default=None, null=True, blank=True)
    serves = models.IntegerField(help_text='Number of portions from base recipe',default=None,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    modified = models.DateTimeField(auto_now=True,editable=False),
    draft = models.BooleanField(default=False)

    class Meta:
        ordering = ['-name']

    def get_absoulte_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name

