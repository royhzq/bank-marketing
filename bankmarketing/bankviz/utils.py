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
            print("COMPARE :",cat_val, option)
            if cat_val  == option:
                data[cat + '_' + option] = 1
            else:
                data[cat + '_' + option] = 0

        del data[cat]

    return data


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