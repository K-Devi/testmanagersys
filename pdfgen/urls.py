from django.urls import path
from .pdf import generate_pdf

urlpatterns = [
    path('pdf-gen/', generate_pdf, name='pdf-gen'),
]

