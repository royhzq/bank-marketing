from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.conf import settings
from .utils import predict

import json


class PredictAPI(APIView):

    def post(self, request, format=None):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            return Response(predict(serializer.data))

class GetColValuesAPI(APIView):

    def post(self, request, format=None):
        serializer = GetColValuesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            col = serializer.data.get('colname')
            col_vals = settings.DATAFRAME[col].values
            response = {
                'column': col,
                'max': col_vals.max(),
                'min': col_vals.min(),
                'values':[ {'value':val } for val in col_vals ]
            }

            return Response(response)


