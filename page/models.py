from django.db import models
from django.utils.text import slugify

STATUS = [
    # sol kısım dbye yazılacak olan
    # sağ kısım kullanıcıya gözükecek
    # Page.objects.filter(status="draft").count()
    ('draft', 'Taslak'),
    ('published', 'Yayınlandi'),
    ('deleted', 'Silindi'),
]

# Create your models here.

class Page(models.Model):
    # title : Hakkımızda / İletişim
    title = models.CharField(max_length=200)
    # slug : (hakkimizda, iletisim) sadece ilk create sirasinda olusmalidir
    slug = models.SlugField(
        max_length=200,
        default="",
        )
    # content : İçerik
    content = models.TextField()
    # cover_image
    cover_image = models.ImageField(
        upload_to='page',
        null = True,
        blank = True,
        )
    # status
    status = models.CharField(
        default="draft",
        choices=STATUS,
        max_length=10,
        )
    # created_at
    created_at = models.DateTimeField(auto_now_add=True)
    # updated_at
    updated_at = models.DateTimeField(auto_now=True)