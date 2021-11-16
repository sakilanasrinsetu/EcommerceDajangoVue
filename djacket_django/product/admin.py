from django.contrib import admin
from django.db import models
from .models import Category, Product

# Register your models here.


# Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

admin.site.register(Product,ProductAdmin)