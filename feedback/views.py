from django.shortcuts import get_object_or_404, render
from .forms import FeedbackForm
from .models import Feedback
from products.models import Product

# Create your views here.
def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
 
        if form.is_valid():
            print("Here's your product..")
            prod=(form.cleaned_data['product'])
            this_session_rating=(form.cleaned_data['rating'])

            if request.user.is_authenticated:
                prod_feedback = Feedback.objects.filter(product=prod)
                num_prod_feedbacks=(prod_feedback.count())
                total_rating=0
                for item in prod_feedback:
                    print(str(item.rating))
                    total_rating+=item.rating

                total_rating+=this_session_rating
                average_rating = total_rating/(num_prod_feedbacks+1)
                average_rating = round(average_rating,1)
                
                print("Average rating is " + str(average_rating))

                #prod_feedback = all_feedback.objects.filter(product=product)
                
                    #print(feedback.product)
                    #print(feedback.rating)
    
        


           
          
            form.save()
        
            return render(request, 'confirm.html')

    else:
        form = FeedbackForm()
        
    return render(request, 'feedback_form.html', {'form': form, })
