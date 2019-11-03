from django.shortcuts import render
from django.conf import settings
from django.http import  HttpResponse, Http404
from .utils import predict, get_pair_values, get_category_success
import json

def data_viz(request):

    # Initial correlation matrix
    df_corr = settings.DATAFRAME.corr()
    corr_cols = list(df_corr.columns)
    corr_data = []
    for x in corr_cols:
        for y in corr_cols:
            val = df_corr.iloc[corr_cols.index(x)][y]
            corr_data.append({
                'x':x,
                'y':y,
                'value':val
            })

    # Initial histogram values - age
    age_vals = settings.DATAFRAME['age'].values
    age_hist = {
        'column': 'age',
        'max': int(age_vals.max()),
        'min': int(age_vals.min()),
        'values':[ {'value':int(val) } for val in age_vals ]
    }

    # Initial pairs values - age / pdays
    pair_data = get_pair_values('age', 'campaign')

    # Initial stacked bar chart data
    stack_data = get_category_success('job')

    context = {
        'corr_data':json.dumps(corr_data),  
        'age_hist':json.dumps(age_hist),
        'pair_data':json.dumps(pair_data),
        'stack_data':json.dumps(stack_data)
    }
    return render(
        request,
        'bankviz/home.html',
        context
    )