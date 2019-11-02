from django.urls import include, path
from .views import data_viz
from .api import PredictAPI, GetColValuesAPI
urlpatterns = [
    path('', data_viz),
    path('api/predict', PredictAPI.as_view()),
    path('api/get_col_values', GetColValuesAPI.as_view())
]