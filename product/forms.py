from django import forms
from .models import Category, Product


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        # fields = '__all__' # Don't use this -- This is for testing
        fields = [
            'title',
            'slug',
            'cover_image',
            'status',
        ]

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__' # Don't use this -- This is for testing
        # exclude = ['title']
        fields = [
            'category',
            'title',
            'slug',
            'cover_image',
            'content',
            'status',
            'stock',
            'price',
        ]