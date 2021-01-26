from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from page.views import index, page_show
from product.views import category_show

urlpatterns = [
    path('', index, name='index'), 
    path('manage/', include('page.urls'),),
    path('cart/', include('cart.urls'),),
    path('admin/', admin.site.urls),
    path('<slug:category_slug>', category_show, name='category_show'),
    path('<slug:page_slug>/', page_show, name='page_show'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)