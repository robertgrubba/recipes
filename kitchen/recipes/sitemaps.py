from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import sitemap
from django.urls import path
from .models import Recipe

class RecipeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(Self):
        return Recipe.objects.filter(draft=False)

    def lastmod(self,obj):
        return obj.created



