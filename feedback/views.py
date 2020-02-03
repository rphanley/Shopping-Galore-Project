from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from accounts.views import clear_messages
from .forms import FeedbackForm
from checkout.models import Order
from products.models import Product


# Create your views here.
@login_required()
def feedback_form(request):
    
    try:
        user_orders = Order.objects.filter(
            username=request.user
        )

    except Order.DoesNotExist:
        user_orders = None

    if user_orders.count() == 0:
        clear_messages(request)
        messages.error(request, "To give feedback, you must be logged in and have products purchased.")
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        # Get the product name, and what rating the user has given it. Average it with the existing rating.
        if form.is_valid():
            feedback_product = (form.cleaned_data['product'])
            feedback_rating = (form.cleaned_data['rating'])

            if request.user.is_authenticated:
                product = get_object_or_404(Product, name=feedback_product)
                current_rating = product.rating
                
                if current_rating > 0:
                    new_rating = (current_rating + feedback_rating)/2
                else:
                    new_rating = feedback_rating

                product.rating = round(new_rating, 1)
                product.save()

            form.save()

            return render(request, 'confirm.html')

    else:
        form = FeedbackForm()

    return render(request, 'feedback_form.html', {'form': form, })
