from rest_framework import serializers
from .models import *


class ChallagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challanges
        fields = ('id', 'Title', 'Social', 'Emotional', 'Study', 'Personal', 'completed', 'students')

class Completed_ChallangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Completed_Challange
        fields = '__all__'
