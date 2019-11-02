from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .utils import predict


import json


class PredictAPI(APIView):

    def post(self, request, format=None):
        serializer = DataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            return Response(predict(serializer.data))

