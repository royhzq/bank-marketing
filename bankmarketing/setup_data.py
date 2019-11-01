#Setup Django environment to access models
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bankmarketing.settings")

import django
django.setup()

import pandas as pd

df = pd.read_csv('data/bank-additional-full.csv', delimiter=';')
print(df)