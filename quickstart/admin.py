from django.contrib import admin

# Register your models here.
from .models import CartItem

admin.site.register(CartItem)

from .models import Customers

admin.site.register(Customers)
