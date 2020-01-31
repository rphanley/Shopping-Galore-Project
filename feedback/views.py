from django.shortcuts import get_object_or_404, render
from .forms import FeedbackForm
from products.models import Product

# Create your views here.
def feedback_form(request, id):
    print(id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            form.save()
            return render(request, 'confirm.html')
    else:
        form = FeedbackForm(initial={'product': id})
    return render(request, 'feedback_form.html', {'form': form})
