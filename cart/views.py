"""Views for view, add, and adjust cart items"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from accounts.views import clear_messages
from products.models import Product
from .models import Cart, CartItem



# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    clear_messages(request)
    if request.user.is_authenticated and not request.session.get('cart_exists'):
        messages.error(
            request, "No cart created yet. Search for products to buy and add them to the cart.")

    if not request.user.is_authenticated:
        messages.error(
            request, "Sorry..you need to register/log in to create a cart.")

    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    if request.user.is_authenticated:
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
    messages.error(request, "Added " + str(quantity) + " of " +
                   "'" + product.name + "'" + " to your cart.")

    return redirect(reverse('products'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))

    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(
                user=request.user
            )
        except Cart.DoesNotExist:
            cart = None

    product = get_object_or_404(Product, pk=id)
    user_cart_items = CartItem.objects.filter(cart=cart)
    user_cart_item = user_cart_items.get(product=product)

    # Update the cart item with the new quantity. If it's 0, delete the item.
    if quantity > 0:
        user_cart_item.quantity = quantity
        user_cart_item.save()
        cart.save()
    else:
        user_cart_item.delete()
        # If there are now no other items remaining in the cart, delete it.
        if user_cart_items.count() == 0:
            cart.delete()

    return redirect(reverse('view_cart'))
