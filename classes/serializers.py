from rest_framework import serializers
from .models import StudentClass
from users.models import CustomUser

class StudentClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentClass
        fields = ('id', 'title')


class StudentClassStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name')