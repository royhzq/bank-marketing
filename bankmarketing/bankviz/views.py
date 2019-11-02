from django.shortcuts import render
from django.conf import settings
from .utils import predict
# Create your views here.

def data_viz(request):

    context = {}
    return render(
        request,
        'bankviz/home.html',
        context
    )