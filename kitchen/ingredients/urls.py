from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from ingredients import views
#from ingredient.views import IngredientListView

urlpatterns = [
        path('', views.IngredientListView.as_view(), name='ingredients'),
        ]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

