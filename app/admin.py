from django.contrib import admin
from .models import Distributeur, Product, Invoice, Invoice_Item

# Register your models here.
admin.site.register(Distributeur)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(Invoice_Item)
