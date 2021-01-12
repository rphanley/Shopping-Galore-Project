from django.contrib import admin
from .models import Cart, CartItem


# Register your models here.
class CartItemAdminInline(admin.TabularInline):
    model = CartItem


class CartAdmin(admin.ModelAdmin):
    inlines = (CartItemAdminInline, )


admin.site.register(Cart, CartAdmin)
