from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from products.models import Product


# Create your views here.
def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
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
                messages.error(request, "You have successfully logged in")
                #Set default session expiry for a logged in user
                request.session.set_expiry(1000000)

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
   
    return render(request, 'profile.html')


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
    

def restore_cart(request):

    #Look for a saved cart in the database if a user is logged in. Restore it if so.
    if request.user.is_authenticated:
        print(request.user.username)
    else:
        print("User not authenticated..")

    if Cart.objects.exists():
        print("Restore cart(s) exist..")
        for cart in Cart.objects.all():
            print(str(cart.user))
            if str(cart.user) == request.user.username:
                print("Found matching cart..")
                request.session['cart'] = {}
                for item in CartItem.objects.filter(cart=cart):
                    print (item.product)
                    print (item.quantity)
                    item_document = {
                            'cart': cart,
                            'product': item.product,
                            'quantity': item.quantity
                    }
                    #request.session['cart'][index] = item_document
                    

        print("Got restore cart..")
    else:
        print("No restore cart exists, or Guest user..")