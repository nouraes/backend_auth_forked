from django.db import models


class StudentClass(models.Model):
    title = models.CharField(max_length=150, default='Class')

    def __str__(self):
        return self.title

# Create your models here.
