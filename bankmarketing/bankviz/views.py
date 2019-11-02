from django.shortcuts import render
from django.conf import settings
from .utils import predict

import json
# Create your views here.

def data_viz(request):

    # Correlation matrix
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

    
    age_vals = settings.DATAFRAME['age'].values
    age_hist = {
        'column': 'age',
        'max': int(age_vals.max()),
        'min': int(age_vals.min()),
        'values':[ {'value':int(val) } for val in age_vals ]
    }

    context = {
        'corr_data':json.dumps(corr_data),
        'age_hist':json.dumps(age_hist)
    }
    return render(
        request,
        'bankviz/home.html',
        context
    )