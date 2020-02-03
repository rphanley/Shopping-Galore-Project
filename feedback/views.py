from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import FeedbackForm
from checkout.models import Order
from products.models import Product


# Create your views here.
@login_required()
def feedback_form(request):
    print(request.user)
    try:
        user_orders = Order.objects.filter(
            username=request.user
        )

    except Order.DoesNotExist:
        messages.error(request, "To give feedback, you must be logged in and have products purchased.")
        return redirect(reverse('index'))

    print(user_orders.count())

    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            feedback_product = (form.cleaned_data['product'])
            feedback_rating = (form.cleaned_data['rating'])

            if request.user.is_authenticated:
                product = get_object_or_404(Product, name=feedback_product)
                current_rating = product.rating
                print(current_rating)
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
