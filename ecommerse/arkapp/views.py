import django.contrib.auth.models
from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.

def home(request):
   return render(request, 'index.html')

def purchase(request):
    
    allprods=[]
    catpods=Product.objects.values('category','id')
    cats={ item['category'] for item in catpods }
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])

    params={'allProds':allprods }
    return render(request,"purchase.html",params)