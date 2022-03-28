from rest_framework import serializers
from . models import alert

class alertSerializer(serializers.ModelSerializer):
    class Meta:
        model = alert
        fields = '__all__'