import datetime
from django_resized import ResizedImageField
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=20, help_text='Ingredient name')
    slug = models.CharField(max_length=20, help_text='Slug of url',default=None,null=True,blank=True)
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    calories = models.IntegerField(help_text='Calories in 100g [g]',default=None)
    fat = models.FloatField(help_text='Fat in 100g [g]',default=None)
    sodium = models.FloatField(help_text='Sodium in 100g [mg]',default=None)
    potassium = models.FloatField(help_text='Potasium in 100g [mg]',default=None)
    carbohydrates = models.FloatField(help_text='Carbohydrates in 100g [mg]',default=None)
    dietaryfiber  = models.FloatField(help_text='Dietary Fiber [g]',default=None)
    sugar = models.FloatField(help_text='Sugars in 100g [g]',default=None)
    protein = models.FloatField(help_text='Protein in 100g [g]',default=None)
    vita = models.FloatField(default=None)
    vitc = models.FloatField(default=None)
    vitb6 = models.FloatField(default=None)
    calcium = models.IntegerField(default=None)
    iron = models.FloatField(default=None)
    zinc = models.FloatField(default=None)
    phosphorous = models.IntegerField(default=None)
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
