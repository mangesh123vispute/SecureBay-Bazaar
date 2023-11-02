import arkapp
from django.contrib import admin
import django.db
from .models import Orders, OrderUpdate
from .models import Product,Orders,OrderUpdate

# Register your models here.
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
