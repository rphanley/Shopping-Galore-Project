from django.shortcuts import render, redirect, reverse
from .models import UserCart

# Create your views here.
def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart

    #TEST CODE
    if request.user.is_authenticated():
            print("User is authenticated, saving cart to database..")
            (user_cart, _) = UserCart.objects.get_or_create(user=request.user)
            user_cart.items = cart.items_serializable
            user_cart.save()
    #END TEST

    return redirect(reverse('index'))


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    