from rest_framework import serializers
from .models import SavingsPlan

class SavingsPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsPlan
        fields = '__all__'