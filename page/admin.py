from page.models import Page
from django.contrib import admin
from django.db import models
from .models import Page, Carousel

class PageAdmin(admin.ModelAdmin):
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

class CarouselAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'title',
        'cover_image',
        'status',
    ]
    list_filter = ['status', ]
    list_editable = list_filter


admin.site.register(Page, PageAdmin)
admin.site.register(Carousel, CarouselAdmin)

# M Db yapisi
# V View / Control
# T Template
# A Admin
# F Forms
# M Message
# S Session
