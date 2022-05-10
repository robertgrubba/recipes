from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, help_text='Category name')
    description = models.TextField()
    image = ResizedImageField(size=[500,300],quality=85,keep_meta=True,upload_to='images/%Y/%m/%d/',default=None,null=True,blank=True)

    def __str__(self):
        return self.name

class Step(models.Model):
    description = models.TextField()
    recipe = models.ForeignKey('Recipe',on_delete=models.SET_NULL,null=True)
    image = ResizedImageField(size=[500,300],quality=85,keep_meta=True,upload_to='images/%Y/%m/%d/',default=None,null=True,blank=True)


class Recipe(models.Model):
    name = models.CharField(max_length=200, help_text='Recipe name')
    description = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.SET_NULL, null=True)
    image = ResizedImageField(size=[500,300],quality=85,keep_meta=True,upload_to='images/%Y/%m/%d/',default=None,null=True,blank=True)
    
    class Meta:
        ordering = ['-name']

    def get_absoulte_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name
