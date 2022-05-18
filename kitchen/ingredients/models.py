import datetime
from django_resized import ResizedImageField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=10)
    slug = models.CharField(max_length=10,help_text='Slug for url', default=None,null=True,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Type, self).save(*args, **kwargs)


class Ingredient(models.Model):
    name = models.CharField(max_length=20, help_text='Ingredient name')
    slug = models.CharField(max_length=20, help_text='Slug for url',default=None,null=True,blank=True)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True,related_name='ingredients')
    ndbn = models.IntegerField(null=True,default=None,blank=True,help_text='Nutrient Data Bank Number')
    calories = models.IntegerField(help_text='Calories in 100g [g]',default=None,null=True,blank=True)
    fat = models.FloatField(help_text='Fat in 100g [g]',default=None,null=True,blank=True)
    monosaturatedfat = models.FloatField(help_text='Monosaturated Fat in 100g [g]',default=None,null=True,blank=True)
    polysaturatedfat = models.FloatField(help_text='Polysaturated Fat in 100g [g]',default=None,null=True,blank=True)
    saturatedfat = models.FloatField(help_text='Saturated Fat in 100g [g]',default=None,null=True,blank=True)
    carbohydrates = models.FloatField(help_text='Carbohydrates in 100g [mg]',default=None,null=True,blank=True)
    dietaryfiber  = models.FloatField(help_text='Dietary Fiber [g]',default=None,null=True,blank=True)
    sugar = models.FloatField(help_text='Sugars in 100g [g]',default=None, null=True,blank=True)
    protein = models.FloatField(help_text='Protein in 100g [g]',default=None,null=True,blank=True)
    alphacarotene = models.FloatField(help_text='Alpha Carotene in 100g [mg]',default=None,null=True,blank=True)
    betacarotene = models.FloatField(help_text='Beta Carotene in 100g [mg]', default=None,null=True,blank=True)
    betacryptoxanthin = models.FloatField(help_text='Beta Cryptoxanthin in 100g [mg]', default=None,null=True,blank=True)
    cholesterol = models.IntegerField(help_text='Cholesterol in 100g [mg]',default=None,null=True,blank=True)
    choline = models.FloatField(help_text='Choline in 100g [mg]',default=None,null=True,blank=True)
    luteinzeaxanthin = models.FloatField(help_text='Lutein and Zeaxanthin in 100g [mg]', default=None,null=True,blank=True)
    lycopene = models.FloatField(help_text='Lycopene in 100g [mg]', default=None,null=True,blank=True)
    vita = models.FloatField(help_text='VitA in 100g [mg]',default=None,null=True,blank=True)
    vita1 = models.FloatField(help_text='Retinol/VitA1 in 100g [mg]',default=None,null=True,blank=True)
    vitc = models.FloatField(default=None,null=True,blank=True)
    vitb1 = models.FloatField(help_text='Thiamin/B1 in 100g [mg]',default=None,null=True,blank=True)
    vitb2 = models.FloatField(help_text='Riboflavin/B2 in 100g [mg]',default=None,null=True,blank=True)
    vitb3 = models.FloatField(help_text='Niacin/VitB3 in 100g [mg]',default=None,null=True,blank=True)
    vitb5 = models.FloatField(help_text='Pantothenic acid/VitB5 in 100g [mg]',default=None,null=True,blank=True)
    vitb6 = models.FloatField(default=None,null=True,blank=True)
    vitb9 = models.FloatField(help_text='Folate/VitB9 in 100g [mg]',default=None,null=True,blank=True)
    vitb12 = models.FloatField(help_text='Vit B12 in 100g [mg]',default=None,null=True,blank=True)
    vite = models.FloatField(help_text='Vit E in 100g [mg]',default=None,null=True,blank=True)
    vitk = models.FloatField(help_text='Vit K in 100g [mg]',default=None,null=True,blank=True)
    calcium = models.IntegerField(help_text='Calcium in 100g [mg]',default=None,null=True,blank=True)
    copper = models.FloatField(help_text='Copper in 100g [mg]',default=None,null=True,blank=True)
    iron = models.FloatField(default=None,null=True,blank=True)
    magnesium = models.FloatField(help_text='Magnesium in 100g [mg]',default=None,null=True,blank=True)
    manganese = models.FloatField(help_text='Manganese in 100g [mg]',default=None,null=True,blank=True)
    phosphorous = models.IntegerField(default=None,null=True,blank=True)
    potassium = models.FloatField(help_text='Potasium in 100g [mg]',default=None,null=True,blank=True)
    selenium = models.FloatField(help_text='Selenium in 100g [mg]',default=None,null=True,blank=True)
    sodium = models.FloatField(help_text='Sodium in 100g [mg]',default=None,null=True,blank=True)
    zinc = models.FloatField(default=None,null=True,blank=True)
    water = models.IntegerField(default=None,null=True,blank=True)
    weight = models.FloatField(help_text='Average weight of piece in grams',default=None,null=True,blank=True)
    teaspoon = models.FloatField(help_text='Weight of teaspoon in grams',default=None,null=True,blank=True) 
    tablespoon = models.FloatField(help_text='Weight of tablespoon in grams',default=None,null=True,blank=True)
    cup = models.IntegerField(help_text='Weight of cup in grams',default=None,null=True,blank=True)
    glass = models.IntegerField(help_text='Weight of glass in grams',default=None,null=True,blank=True)
    bunch = models.IntegerField(help_text='Weight of average bunch of product',default=None,null=True,blank=True)
    image = ResizedImageField(size=[500,300],quality=85,keep_meta=True,upload_to='images/%Y/%m/%d/',default=None,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    modified = models.DateTimeField(auto_now=True,editable=False)
    draft = models.BooleanField(default=True)

    class Meta:
        ordering = ['-name']

    def get_absolute_url(self):
        return reverse('ingredient', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Ingredient, self).save(*args, **kwargs)
    

    def __str__(self):
        return self.name
