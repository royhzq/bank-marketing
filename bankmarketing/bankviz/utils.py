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
    model = settings.LOGISTIC_MODEL

    data['emp_var_rate'] = 0.08188550063125165
    data['cons_price_idx'] = 93.5756643682626
    data['cons_conf_idx'] = -40.50260027192386
    data['euribor3m'] = 3.621290812858114
    data['nr_employed'] = 5167.035910944936
    data = convert_dummy(data)
    data = { k:[v] for k,v in data.items() }

    df = pd.DataFrame.from_dict(data)
    df = df[settings.X_TRAIN_COLS]

    x_pred = scaler.transform(df)
    prediction = model.predict_proba(x_pred)[0]
    # Returns  [prob of 0, prob of 1]
    return prediction