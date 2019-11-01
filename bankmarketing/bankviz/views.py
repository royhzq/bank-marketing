from django.shortcuts import render
from django.conf import settings
# Create your views here.

def data_viz(request):

    df = settings.DATAFRAME
    print(df)
    context = {
        'test': df['y'].value_counts()
    }
    return render(
        request,
        'bankviz/home.html',
        context
    )