"""View for the Products model"""
from django.shortcuts import render
from django.contrib import messages
from accounts.views import clear_messages
from .models import Product

# Create your views here.
def all_products(request):
    """Display all products in the database"""
    clear_messages(request)
    products = Product.objects.all()

    if request.user.is_authenticated:
        messages.error(request,
                       "You can buy products, or save your shopping cart until you log in again.")
    else:
        messages.error(request,
                       "You are not logged in. You can view products. Register/log in to shop, or save your shopping cart until next time!")

    return render(request, "products.html", {"products": products})
