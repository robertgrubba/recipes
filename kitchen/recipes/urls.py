from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from recipes import views

urlpatterns = [
        path('', views.RecipeListView.as_view(), name='recipes'),
        path('<slug:slug>', views.RecipeDetailView.as_view(), name='recipe'),
        path('calc/',views.calc,name='calculate'),
        path('categories/', views.CategoryListView.as_view(), name='categories'),
        path('categories/<slug:slug>', views.CategoryDetailView.as_view(), name='category'),
        ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

