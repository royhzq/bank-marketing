from django.urls import include, path
from .views import data_viz
from .api import PredictAPI
urlpatterns = [
    path('data', data_viz),
    path('api/predict', PredictAPI.as_view())
]