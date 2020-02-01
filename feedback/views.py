from django.shortcuts import get_object_or_404, render
from .forms import FeedbackForm
from products.models import Product

# Create your views here.
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            print("Here's your product..")
            print (form.cleaned_data['product'])
          
            form.save()
        
            return render(request, 'confirm.html')

    else:
        form = FeedbackForm()
        
    return render(request, 'feedback_form.html', {'form': form, })
