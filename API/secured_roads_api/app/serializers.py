from rest_framework import serializers
from . models import x

class xSerializer(serializers.ModelSerializer):
    class Meta:
        model = x
        fields = '__all__'