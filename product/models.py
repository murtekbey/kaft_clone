from django.db import models
from page.models import DEFAULT_STATUS, STATUS

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        default="",
        )
    cover_image = models.ImageField(
        upload_to='category',
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

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
        )
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
    price = models.FloatField()
    stock = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(
        default=DEFAULT_STATUS,
        choices=STATUS,
        max_length=10,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)