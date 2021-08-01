from django.contrib import admin
from .models import Challanges


# class ChallangesAdmin(admin.ModelAdmin):
#     list_display = ('Title', 'Social', 'Emotional', 'Study', 'Personal', 'completed') #removed for debug



admin.site.register(Challanges)
# Register your models here.
