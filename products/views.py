from django.shortcuts import render
from .models import Product
from django.contrib import messages

# Create your views here.
def all_products(request):
    products = Product.objects.all()

    if request.user.is_authenticated:
        messages.info(request, "Logged in as '" + user_name + "'. You can buy products, or save your shopping cart until you log in again.")
    else:
        messages.info(request, "Logged in as Guest. You can view products. Register/log in to shop, or save your shopping cart until next time!")

    return render(request, "products.html", {"products": products})
    