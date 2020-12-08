from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'slug',
        'status',
        'updated_at',
    )
    list_filter = ('status',)
    list_editable = (
        'title',
        'status',
    )

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'pk',
        'title',
        'price',
        'stock',
        'slug',
        'status',
        'updated_at',
    )
    list_filter = ('status',)
    list_editable = (
        'title',
        'status',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)