from django.urls import include, path
from .views import data_viz

urlpatterns = [
    path('data', data_viz)
]