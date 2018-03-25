from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from app.alumno.views import index

urlpatterns = [
    url(r'^$', index),
]
