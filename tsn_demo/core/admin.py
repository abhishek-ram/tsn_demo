from django.contrib import admin
from .models import Product, Rating


class RatingInlineAdmin(admin.TabularInline):
    model = Rating


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [RatingInlineAdmin,]

