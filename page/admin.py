from page.models import Page
from django.contrib import admin
from django.db import models
from .models import Page, Carousel

class PageModify(admin.ModelAdmin):
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
        'status',
        'title',
)


admin.site.register(Page, PageModify)
admin.site.register(Carousel)

# M Db yapisi
# V View / Control
# T Template
# A Admin
# F Forms
# M Message
# S Session
