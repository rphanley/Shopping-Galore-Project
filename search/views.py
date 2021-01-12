"""View for the search function"""
from django.shortcuts import render
from products.models import Product


# Create your views here.
def do_search(request):
    """Return products.html with the product list filtered by the search text"""
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})