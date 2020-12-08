from django.contrib.admin.sites import DefaultAdminSite
from django.db import models
from django.utils.text import slugify

DEFAULT_STATUS = 'draft'

STATUS = [
    # sol kısım dbye yazılacak olan
    # sağ kısım kullanıcıya gözükecek
    # Page.objects.filter(status="draft").count()
    ('draft', 'Taslak'),
    ('published', 'Yayınlandı'),
    ('deleted', 'Silindi'),
]

# Page
class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        default="",
        )
    content = models.TextField()
    cover_image = models.ImageField(
        upload_to='page',
        null = True,
        blank = True,
        )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Carousel
class Carousel(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    cover_image = models.ImageField(
        upload_to='carousel',
        null=True,
        blank=True,
    )
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)