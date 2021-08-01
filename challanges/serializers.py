from rest_framework import serializers
from .models import Challanges


class ChallagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challanges
        fields = ('id', 'Title', 'Social', 'Emotional', 'Study', 'Personal', 'completed', 'students')
