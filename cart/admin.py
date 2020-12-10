from django.contrib import admin
from .models import ShoppingCart, ShoppingCartItem

class ShoppingCartAdmin():
    pass

class ShoppingCartItemAdmin():
    pass

admin.site.register(ShoppingCart,)
admin.site.register(ShoppingCartItem,)