from django.contrib import admin
from django.urls import path

from django.conf.urls import url, include
from app.alumno.views import index, alumno_view

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^registro$', alumno_view, name='alumno_crear'),
]
