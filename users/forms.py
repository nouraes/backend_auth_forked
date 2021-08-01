# users/forms.pyfrom django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser
from django import forms

ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('Teacher', 'Teacher'),
    ('Student', 'Student'),
    ('Principal', 'Principal'),
    ('Caretaker', 'Caretaker'),
]


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    role = forms.CharField(widget=forms.Select(choices=ROLE_CHOICES))

    class Meta:
        model = CustomUser
        fields = ('email', 'role')  # added 'role' for debug


class CustomUserChangeForm(UserChangeForm):
    role = forms.CharField(widget=forms.Select(choices=ROLE_CHOICES))

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
