from ast import Return
from django.http import HttpResponse 
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('homepage')
    return render(request, 'index.htm')