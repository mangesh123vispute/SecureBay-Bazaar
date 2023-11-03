import arkapp
import django.conf
import django.contrib.auth
import django.contrib.auth.models
from django.shortcuts import render
from django.http import HttpResponse

from .models import Product,Orders
from .models import OrderUpdate
from math import ceil
from django.contrib import messages
from django.shortcuts import redirect
from arkapp import keys
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
import json
from django.conf import settings


MERCHANT_KEY=keys.MK
# Create your views here.

def home(request):
    allprods=[]
    catpods=Product.objects.values('category','id')
    cats={ item['category'] for item in catpods }
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])

    params={'allProds':allprods }
    
    return render(request, 'index.html',params)

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
   
    if request.method=="POST":

        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
         

        Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
        thank = True
        # payment integration
        
        id = Order.order_id
        oid=str(id)+"SecureBuy"
        oid=str(id)
        param_dict = {

            'MID': keys.MID,
            'ORDER_ID': oid,
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')


@csrf_exempt
def handlerequest(request):

    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
            a=response_dict['ORDERID']
            b=response_dict['TXNAMOUNT']
            rid=a.replace("SecureBuy","")
           
            # print(rid)
            filter2= Orders.objects.filter(order_id=rid)
           
            print(filter2)
            print(a,b)
            for post1 in filter2:

                post1.oid=a
                post1.amountpaid=b
                post1.paymentstatus="PAID"
                post1.save()
            print("run agede function")
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})


def tracker(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('arkauth/login/')
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{no orders}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'tracker.html')


def about(request):
    return render(request, 'about.html')