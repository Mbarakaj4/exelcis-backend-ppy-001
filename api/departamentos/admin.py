"""
Admin

admin model registration
"""
from django.contrib import admin
from .models import Ciudad, Pronostico

admin.site.register(Ciudad)
admin.site.register(Pronostico)