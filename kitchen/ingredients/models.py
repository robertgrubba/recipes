from django_resized import ResizedImageField
from django.db import models
from django.urls import reverse
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=20, help_text='Ingredient name')
    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)
    calories = models.IntegerField(help_text='Calories in 100g [g]')
    fat = models.FloatField(help_text='Fat in 100g [g]')
    sodium = models.FloatField(help_text='Sodium in 100g [mg]')
    potasium = models.FloatField(help_text='Potasium in 100g [mg]')
    carbohydrates = models.FloatField(help_text='Carbohydrates in 100g [mg]')
    dietaryfiber  = models.FloatField(help_text='Dietary Fiber [g]')
    sugar = models.IntegerField(help_text='Sugars in 100g [g]')
    protein = models.FloatField(help_text='Protein in 100g [g]')
    vita = models.FloatField()
    vitc = models.FloatField()
    vitb6 = models.FloatField(default=None)
    calcium = models.IntegerField()
    iron = models.FloatField()
    zinc = models.FloatField(default=None)
    phosphorous = models.IntegerField(default=None)
    water = models.IntegerField(default=None)
    weight = models.IntegerField()
    image = ResizedImageField(size=[500,300],quality=85,keep_meta=True,upload_to='images/%Y/%m/%d/',default=None,null=True,blank=True)
    
    class Meta:
        ordering = ['-name']

    def get_absoulte_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name
