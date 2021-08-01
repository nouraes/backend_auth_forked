from users.serializers import *
from users.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class StudentProfileView(APIView):

    def get(self, format=None):
        students = StudentProfile.objects.all()
        serializer = StudentProfileSerializer(students, many=True)
        return Response(serializer.data)