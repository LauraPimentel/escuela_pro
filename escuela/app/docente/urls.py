from django.contrib import admin
from django.urls import path

from django.conf.urls import url
from app.docente.views import index_docente

urlpatterns = [
    url(r'^index$', index_docente)
]
