"""kitchen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from recipes.sitemaps import RecipeSitemap
from ingredients.sitemaps import IngredientSitemap
from django.urls import include
from django.views.generic.base import TemplateView

sitemaps = {
        'recipe': RecipeSitemap,
        'ingredient': IngredientSitemap,
}


from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [
        path('',views.index,name='index'),
        path('about/',views.about,name='about'),
        path('products/',views.products,name='products'),
        path('store/',views.store,name='store'),
        path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
        path('ingredients/', include('ingredients.urls')),
        path('recipes/', include('recipes.urls')),
        path('sitemap.xml',sitemap,{'sitemaps': sitemaps }),
        ]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

