from django.shortcuts import render
from .models import Language
from rest_framework import viewsets
from .serializer import LanguageSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = 'slug'
