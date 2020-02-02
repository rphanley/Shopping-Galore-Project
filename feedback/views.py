from django.shortcuts import get_object_or_404, render
from .forms import FeedbackForm
from .models import Feedback
from products.models import Product

# Create your views here.
def feedback_form(request):
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
                print("New product rating is " + str(product.rating))
                product.save()
                
                

   
    
        


           
          
            form.save()
        
            return render(request, 'confirm.html')

    else:
        form = FeedbackForm()
        
    return render(request, 'feedback_form.html', {'form': form, })
