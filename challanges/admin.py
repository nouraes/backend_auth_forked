from django.contrib import admin
from .models import *


# class ChallangesAdmin(admin.ModelAdmin):
#     list_display = ('Title', 'Social', 'Emotional', 'Study', 'Personal', 'completed') #removed for debug



admin.site.register(Challanges)
admin.site.register(Completed_Challange)
# Register your models here.
