from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from django.conf import settings
import pandas as pd
import numpy as np

def convert_dummy(data):

    # Manual conversion of categorical user inputs to dummies

    for cat in settings.CATEGORICAL:
        cat_val = data[cat] # Value from user
        for option in settings.CATEGORICAL_VALUES[cat]:
            if cat_val  == option:
                data[cat + '_' + option] = 1
            else:
                data[cat + '_' + option] = 0

        del data[cat]

    return data

def get_pair_values(xcol, ycol):

    x_vals = settings.DATAFRAME[xcol].values
    y_vals = settings.DATAFRAME[ycol].values
    z_vals = settings.DATAFRAME['y_vals'].apply(lambda x: "Subscribed" if x==1 else "Did Not Subscribe").values

    x_vals_max, x_vals_min = max(x_vals), min(x_vals)
    y_vals_max, y_vals_min = max(y_vals), min(y_vals)
    
    # For D3 Axes
    x_range_max = float(x_vals_max*1.05 if x_vals_max > 0 else x_vals_max*0.95)
    y_range_max = float(y_vals_max*1.05 if y_vals_max > 0 else y_vals_max*0.95)
    x_range_min = float(x_vals_min*1.05 if x_vals_min < 0 else x_vals_min*0.95)
    y_range_min = float(y_vals_min*1.05 if y_vals_min < 0 else y_vals_min*0.95)

    values = []
    for row in zip(x_vals, y_vals, z_vals):
        values.append({
            "x":float(row[0]),
            "y":float(row[1]),
            "success":row[2]
        })

    response = {
        "x_name":xcol,
        "y_name":ycol,
        "x_min":x_range_min,
        "x_max":x_range_max,
        "y_min":y_range_min,
        "y_max":y_range_max,
        "values": values
    }

    return response

def get_category_success(category):

    # Given categorical variable
    # Return dict for CategorySuccessAPI 
    dfx = settings.DATAFRAME.groupby(category).apply(lambda x: pd.Series({
        'success': x['y_vals'].sum(),
        'failure': len(x['y_vals']) -x['y_vals'].sum()
    })).reset_index()
    response = {
        "keys":list(dfx[category].values),
        "values": [
            {
                "name":r[category],
                "Did Not Subscribe":r['failure'],
                "Subscribed":r['success']
            } \
            for i, r in dfx.iterrows() 
        ]
    }

    return response

def predict(data):

    # For external data , use mean of dataset as placeholder values for now

    scaler  = settings.SCALER
    log_model = settings.LOGISTIC_MODEL
    rf_model = settings.RANDOM_FORESTS_MODEL
    xgb_model = settings.XGB_MODEL

    data['emp_var_rate'] = 0.08188550063125165
    data['cons_price_idx'] = 93.5756643682626
    data['cons_conf_idx'] = -40.50260027192386
    data['euribor3m'] = 3.621290812858114
    data['nr_employed'] = 5167.035910944936
    data = convert_dummy(data)
    data = { k:[v] for k,v in data.items() }

    df = pd.DataFrame.from_dict(data)
    df = df[settings.X_TRAIN_COLS]

    x_scaled = scaler.transform(df)
    log_pred = log_model.predict_proba(x_scaled)[0][1]
    rf_pred = rf_model.predict_proba(x_scaled)[0][1]
    xgb_pred = xgb_model.predict_proba(x_scaled)[0][1]

    results = [
        {'name':'Aggregate', 'value':sum([log_pred, rf_pred, xgb_pred])/3},
        {'name':'XGBoost', 'value':xgb_pred},
        {'name':'Random Forests', 'value':rf_pred},
        {'name':'Logistic Regression', 'value':log_pred},
    ]
    # Returns  prob of success
    return results