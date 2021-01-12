"""checkout view"""
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.utils import timezone
from accounts.views import clear_messages
from cart.models import Cart, CartItem
import stripe
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem



# Create your views here.

stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """Handle address and credit card details input for cart checkout"""
    clear_messages(request)
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.username = request.user
            order.save()

            try:
                cart = Cart.objects.get(
                    user=request.user
                )
            except Cart.DoesNotExist:
                messages.error(request, "No cart created yet!")
                cart = None

            total = 0
            for item in CartItem.objects.filter(cart=cart):
                product = item.product
                quantity = item.quantity
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                clear_messages(request)
                messages.error(request, "You have successfully paid!")
                for item in CartItem.objects.filter(cart=cart):
                    item.delete()

                cart.delete()
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        if request.session.get('cart_exists'):
            payment_form = MakePaymentForm()
            order_form = OrderForm()

    return render(request, "checkout.html",
                  {'order_form': order_form, 'payment_form': payment_form,
                   'publishable': settings.STRIPE_PUBLISHABLE})
