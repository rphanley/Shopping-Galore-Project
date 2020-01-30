from cart.models import Cart, CartItem


def cart_contents(request):
    """
    Ensures that the cart contents are available when rendering
    every page
    """
    cart_items = []
    total = 0
    product_count = 0
    cart=None
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(
                        user=request.user
            )
            request.session['cart_exists'] = True
        except Cart.DoesNotExist:
                        print("No cart exists for user..")
                        request.session['cart_exists'] = False
                        

    for item in CartItem.objects.filter(cart=cart):
        test_id = item.product.id
        product = item.product
        total += item.quantity * product.price
        product_count += item.quantity
        cart_items.append({'id': test_id, 'quantity': item.quantity, 'product': product})

        
    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
    