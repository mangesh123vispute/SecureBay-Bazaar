import django.contrib.auth
import django.contrib.auth.models
from django.shortcuts import render
from .models import Product
from math import ceil
from django.contrib import messages
from django.shortcuts import redirect
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

def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"login and try again")
        return redirect("/arkauth/login")
    return render(request,'checkout.html')
