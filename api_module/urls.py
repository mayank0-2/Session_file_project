"""
URL configuration for Session_file_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from api_module.sessionHandler import create_session, delete_session
from api_module.fileHandler import file_handler

urlpatterns = [
    path('v1/create-session', create_session.as_view(), name = "CreateSession"),
    path('v1/delete-session', delete_session.as_view(), name ='DeleteSession'),
    path('v1/upload-file/<str:session_id>', file_handler.as_view(), name = "UploadFile"),
]
