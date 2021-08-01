from django.contrib import admin
from .models import StudentClass

# class CustomClassesAdmin(UserAdmin):
#     list_display = ('')


admin.site.register(StudentClass)
