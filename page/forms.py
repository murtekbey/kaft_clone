from django import forms
from .models import Carousel


class CarouselModelForm(forms.ModelForm):
    class Meta:
        model = Carousel
        # fields = '__all__' # Don't use this -- This is for testing
        fields = [
            'title',
            'cover_image',
        ]