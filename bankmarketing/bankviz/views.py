from django.shortcuts import render
from django.conf import settings
from .utils import predict
# Create your views here.

def data_viz(request):

    df = settings.DATAFRAME
    prediction = predict()
    context = {
        'test': df['y'].value_counts(),
        'prediction':prediction
    }
    return render(
        request,
        'bankviz/home.html',
        context
    )