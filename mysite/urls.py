"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from challanges.views import TeacherChallangesView, StudentChallangesView, ChallangeView,get_report
from classes.views import StudentClassView, StudentClassStudentsView
from users.views import StudentProfileView
from django.contrib.auth import logout
from django.urls import path
from chat.views import *

urlpatterns = [
    # Chat

    #path('',index, name='index'),
    path('chat/', chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', message_list, name='message-detail'),
    path('api/messages/', message_list, name='message-list'),
    #path('logout/', logout, {'next_page': 'index'}, name='logout'), #temp disablewd
    path('register/', register_view, name='register'),

    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/teacher/classes/', StudentClassView.as_view()),
    path('api/v1/teacher/classes/<int:student_class_id>/', StudentClassStudentsView.as_view()),
    path('api/v1/teacher/classes/<int:student_class_id>/student/<int:student_id>/challanges/', TeacherChallangesView.as_view()),
    #path('api/v1/teacher/classes/<int:student_class_id>/student/<int:student_id>/challanges/<int:challange_id>', ChallangeView.as_view()), #for debug
    path('api/v1/teacher/challanges/', TeacherChallangesView.as_view()),
    path('api/v1/students/challanges/', StudentChallangesView.as_view()),
    path('api/v1/students/', StudentProfileView.as_view()),
    path('api/students/report/', get_report)
]