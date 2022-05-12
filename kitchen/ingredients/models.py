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
        super(Ingredient, self).save(*args, **kwargs)


class Ingredient(models.Model):
    name = models.CharField(max_length=20, help_text='Ingredient name')
    slug = models.CharField(max_length=20, help_text='Slug for url',default=None,null=True,blank=True)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True,related_name='ingredients')
    calories = models.IntegerField(help_text='Calories in 100g [g]',default=None)
    fat = models.FloatField(help_text='Fat in 100g [g]',default=None)
    monosaturatedfat = models.FloatField(help_text='Monosaturated Fat in 100g [g]',default=None,null=True,blank=True)
    polysaturatedfat = models.FloatField(help_text='Polysaturated Fat in 100g [g]',default=None,null=True,blank=True)
    saturatedfat = models.FloatField(help_text='Saturated Fat in 100g [g]',default=None,null=True,blank=True)
    carbohydrates = models.FloatField(help_text='Carbohydrates in 100g [mg]',default=None)
    dietaryfiber  = models.FloatField(help_text='Dietary Fiber [g]',default=None)
    sugar = models.FloatField(help_text='Sugars in 100g [g]',default=None)
    protein = models.FloatField(help_text='Protein in 100g [g]',default=None)
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
    vitb6 = models.FloatField(default=None,null=True,blank=True)
    vitb12 = models.FloatField(help_text='Vit B12 in 100g [mg]',default=None,null=True,blank=True)
    vite = models.FloatField(help_text='Vit E in 100g [mg]',default=None,null=True,blank=True)
    vitk = models.FloatField(help_text='Vit K in 100g [mg]',default=None,null=True,blank=True)
    calcium = models.IntegerField(help_text='Calcium in 100g [mg]',default=None)
    copper = models.FloatField(help_text='Copper in 100g [mg]',default=None,null=True,blank=True)
    iron = models.FloatField(default=None)
    magnesium = models.FloatField(help_text='Magnesium in 100g [mg]',default=None,null=True,blank=True)
    phosphorous = models.IntegerField(default=None)
    potassium = models.FloatField(help_text='Potasium in 100g [mg]',default=None,null=True,blank=True)
    selenium = models.FloatField(help_text='Selenium in 100g [mg]',default=None,null=True,blank=True)
    sodium = models.FloatField(help_text='Sodium in 100g [mg]',default=None)
    zinc = models.FloatField(default=None)
    water = models.IntegerField(default=None)
    weight = models.IntegerField()
    image = ResizedImageField(size=[500,300],quality=85,keep_meta=True,upload_to='images/%Y/%m/%d/',default=None,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,editable=False,null=True)
    modified = models.DateTimeField(auto_now=True,editable=False)
    draft = models.BooleanField(default=False)

    class Meta:
        ordering = ['-name']

    def get_absoulte_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Ingredient, self).save(*args, **kwargs)
    

    def __str__(self):
        return self.name
