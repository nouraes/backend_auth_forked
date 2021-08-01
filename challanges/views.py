from django.shortcuts import render
from rest_framework import generics
from .serializers import ChallagesSerializer
from .models import Challanges
from rest_framework.permissions import IsAuthenticated

class TeacherChallangesView(generics.ListCreateAPIView):
    queryset = Challanges.objects.all()
    ordering = ['-created']
    serializer_class = ChallagesSerializer


class StudentChallangesView(generics.ListCreateAPIView):
    ordering = ['-created']
    serializer_class = ChallagesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Challanges.objects.filter(students__pk=self.request.user.pk)

#############for debug#############################################################################
class ChallangeView(generics.ListCreateAPIView):
    #ordering = ['-created']
    serializer_class = ChallagesSerializer

    def get_queryset(self):
        return Challanges.objects.filter(challanges_id=self.kwargs['challange_id'])