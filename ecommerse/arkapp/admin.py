import arkapp
from django.contrib import admin
import django.db
from .models import Product

# Register your models here.
admin.site.register(Product)