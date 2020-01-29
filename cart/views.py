from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Cart, CartItem
from products.models import Product


# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    if request.session.get('cart_exists')==False:
        messages.error(request, "No cart created yet. Search for products to buy and add them to the cart.")
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    db_cart, created = Cart.objects.get_or_create(
            user=request.user
    )
    db_cart.save()
    product = get_object_or_404(Product, pk=id)
    db_cart_item = CartItem(
            cart=db_cart,
            product=product,
            quantity=quantity
    )
    db_cart_item.save()


    return redirect(reverse('index'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))

    try:
        cart = Cart.objects.get(
                    user=request.user
        )
    except Cart.DoesNotExist:
                    print("No cart exists for user..")
                    cart=None

    product = get_object_or_404(Product, pk=id)
    user_cart_items = CartItem.objects.filter(cart=cart)
    user_cart_item = user_cart_items.get(product=product)
    user_cart_item.quantity = quantity
    user_cart_item.save()
    cart.save()

    return redirect(reverse('view_cart'))
    