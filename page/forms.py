from django import forms
from .models import Carousel, Page


class CarouselModelForm(forms.ModelForm):
    class Meta:
        model = Carousel
        # fields = '__all__' # Don't use this -- This is for testing
        fields = [
            'title',
            'cover_image',
            'status',
        ]

class PageModelForm(forms.ModelForm):
    class Meta:
        model = Page
        # fields = '__all__' # Don't use this -- This is for testing
        # exclude = ['title']
        fields = [
            'title',
            'cover_image',
            'content',
            'status',
        ]