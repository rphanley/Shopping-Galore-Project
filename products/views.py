from django.shortcuts import render
from .models import Product
from django.contrib import messages

# Create your views here.
def all_products(request):
    products = Product.objects.all()

    #If the user has not logged in, set the session to expire in 60 seconds and post a message requesting login.
    user_name = request.user.username
    if (user_name == ""):
        messages.warning(request, "Logged in as Guest. You can view products. Register or log in to buy products, or save your shopping cart.")
        request.session.set_expiry(60)
    else:
        messages.info(request, "Logged in as " + user_name + ". You can buy products, or save your shopping cart until you log in again.")

    return render(request, "products.html", {"products": products})
    