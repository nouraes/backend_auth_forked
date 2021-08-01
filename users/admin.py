from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser, StudentProfile, TeacherProfile
#from challanges/models.py import Challanges



# Student Profile
class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    can_delete = False
    verbose_name_plural = 'student_profile'

# Teacher Profile
class TeacherProfileInline(admin.StackedInline):
    model = TeacherProfile
    can_delete = False
    verbose_name_plural = 'teacher_profile'

class CustomUserAdmin(UserAdmin):
    inlines = [StudentProfileInline, TeacherProfileInline]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (
            'role',)}),
    )


    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': (
            'email', 'role','first_name', 'last_name')}),
    )
    list_display = ['email', 'role']


admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.


# fieldsets = UserAdmin.fieldsets
# fieldsets = (
#     (None, {
#         'fields': ('email', 'password1', 'content', 'sites')
#     }))