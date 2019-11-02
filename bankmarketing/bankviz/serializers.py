from rest_framework import serializers
from django.conf import settings

class DataSerializer(serializers.Serializer):

    age = serializers.IntegerField(min_value=17, max_value=98)
    job = serializers.ChoiceField(choices=settings.CATEGORICAL_CHOICES['job'])
    marital = serializers.ChoiceField(choices=settings.CATEGORICAL_CHOICES['marital'])
    education = serializers.ChoiceField(choices=settings.CATEGORICAL_CHOICES['education'])
    default = serializers.ChoiceField(choices=settings.CATEGORICAL_CHOICES['default'])
    housing = serializers.ChoiceField(choices=settings.CATEGORICAL_CHOICES['housing'])
    loan = serializers.ChoiceField(choices=settings.CATEGORICAL_CHOICES['loan'])
    contact = serializers.ChoiceField(choices=settings.CATEGORICAL_CHOICES['contact'])
    month = serializers.ChoiceField(choices=settings.CATEGORICAL_CHOICES['month'])
    day_of_week = serializers.ChoiceField(choices=settings.CATEGORICAL_CHOICES['day_of_week'])
    campaign = serializers.IntegerField(min_value=0)
    pdays = serializers.IntegerField(min_value=0)
    previous = serializers.IntegerField(min_value=0)
    poutcome = serializers.ChoiceField(choices=settings.CATEGORICAL_CHOICES['poutcome'])
    # emp_var_rate = serializers.CharField()
    # cons_price_idx = serializers.CharField()
    # cons_conf_idx = serializers.CharField()
    # euribor3m = serializers.CharField()
    # nr_employed = serializers.CharField()

class GetColValuesSerializer(serializers.Serializer):

    colname = serializers.CharField()
