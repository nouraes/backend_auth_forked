from django.db import models
from users.models import CustomUser
# Create your models here.

class Teachers(models.Model):
    teacher_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)