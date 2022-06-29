from django.shortcuts import render

# Create your views here.
def product_list(request):
    render(request, product_list.html)