"""accounts.views, all account handling and the clear_messages function"""
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from checkout.models import Order, OrderLineItem
from cart.models import Cart
from .forms import UserLoginForm, UserRegistrationForm


# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have logged out. Visit us again soon!')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                welcome_message = "Welcome back, " + request.user.username + "!"


                if Cart.objects.filter(user=request.user).exists():
                    welcome_message += " You have an existing cart, click on Cart above to view it."

                messages.error(request, welcome_message)

                if request.GET and request.GET['next'] != '':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('products'))
            else:
                user_form.add_error(
                    None, "Sorry..your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile and order history for the logged in user"""

    # Get the order history for the current user
    try:
        user_orders = Order.objects.filter(
            username=request.user
        )

    except Order.DoesNotExist:
        user_orders = None

    # Build the userOrders dictionary (sample below) to pass the order history to the profile.html template
    if user_orders != None:
        orders = user_orders
        list_user_orders = []

        for single_order in orders:
            dict_user_order = {}
            list_user_order = []
            order_total = 0
            for item in OrderLineItem.objects.filter(order=single_order):
                dict_order_line_item = {'quantity': str(
                    item.quantity), 'product': item.product.name, 'price': str(item.product.price)}
                order_total += (item.product.price*item.quantity)
                list_user_order.append(dict_order_line_item)

            dict_user_order = {'id': single_order.id, 'date': str(
                single_order.date), 'total': str(order_total), 'order_lines': list_user_order}
            list_user_orders.append(dict_user_order)

        # SAMPLE OF userOrders DICTIONARY:
        # {'id': 15, 'date': '2020-01-29', 'total': '20000.00',
        #  'order_lines': [{'quantity': '1', 'product': 'Product 1', 'price': '1000.00'},
        #                  {'quantity': '2', 'product': 'Product 2', 'price': '2000.00'},
        #                  {'quantity': '3', 'product': 'Product 3', 'price': '5000.00'}
        # ]}

    return render(request, 'profile.html', {"userOrders": list_user_orders})


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            clear_messages(request)

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered!")
                return redirect(reverse('products'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)


def clear_messages(request):
    """Clear the message string before displaying a new message in the next view"""
    storage = messages.get_messages(request)
    storage.used = True
