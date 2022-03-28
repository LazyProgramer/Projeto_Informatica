from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import alert
from . serializers import alertSerializer

class alertList(APIView):
    def get(self, request):
        all_alerts = alert.objects.all()
        serializer = alertSerializer(all_alerts, many=True)
        return Response(serializer.data)
    def post(self):
        pass