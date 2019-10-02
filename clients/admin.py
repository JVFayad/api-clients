from django.contrib import admin
from .models import Client, Review

# Add models to Admin
admin.site.register(Client)
admin.site.register(Review)