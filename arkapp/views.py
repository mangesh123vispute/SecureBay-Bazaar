import arkapp
import django.conf
import django.contrib.auth
import django.contrib.auth.models
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django.http import HttpResponse
from ecommerse.settings import EMAIL_HOST_USER
from .models import Orders, Product, Profile
from .models import OrderUpdate
from math import ceil
from django.contrib import messages
from django.shortcuts import redirect
from arkapp import keys
from django.views.decorators.csrf import csrf_exempt
from PayTm import Checksum
import json
from django.conf import settings
from django.contrib.auth import authenticate
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserUpdateForm,ProfileUpdateForm
from .models import Profile
import razorpay
from django.http import HttpResponseBadRequest



MERCHANT_KEY=keys.MK
# Create your views here.

def home(request):
    allprods=[]
    allprof=Profile.objects.all()
    catpods=Product.objects.values('category','id')
    cats={ item['category'] for item in catpods }
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        nSlides=n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nSlides),nSlides])

    params={'allProds':allprods ,'allprof':allprof}
    
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

# razorpay integration

# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
 
 
def homepage(request):
    currency = 'INR'
    amount = 20000  # Rs. 200
 
    # Create a Razorpay Order
    razorpay_order = razorpay_client.order.create(dict(amount=amount,
                                                       currency=currency,
                                                       payment_capture='0'))
 
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'paymenthandler/'
 
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = settings.RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
 
    return render(request, 'razorpay.html', context=context)
 
 
# we need to csrf_exempt this url as
# POST request will be made by Razorpay
# and it won't have the csrf token.
@csrf_exempt
def paymenthandler(request):
 
    # only accept POST request.
    if request.method == "POST":
        try:
           
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
 
            # verify the payment signature.
            result = razorpay_client.utility.verify_payment_signature(
                params_dict)
            if result is not None:
                amount = 20000  # Rs. 200
                try:
 
                    # capture the payemt
                    razorpay_client.payment.capture(payment_id, amount)
 
                    # render success page on successful caputre of payment
                    return render(request, 'paymentsuccess.html')
                except:
 
                    # if there is an error while capturing payment.
                    return render(request, 'paymentfail.html')
            else:
 
                # if signature verification fails.
                return render(request, 'paymentfail.html')
        except:
 
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
       # if other than POST request is made.
        return HttpResponseBadRequest()

# end of razorpay integration

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
        return redirect('/arkauth/login/')
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


def SendMessage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email_from = request.POST.get('email')
        password = request.POST.get('pass')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
    
        user = authenticate(request, username=email_from, password=password)

        
        if user is not None:
            recipient_list=[settings.EMAIL_HOST_USER]
            send_mail(subject,message,email_from,recipient_list)
          
            return HttpResponse("Your message has been sent. Thank you!")
        else:
            return HttpResponse("Authentication failed. Please login first.")
    
    return render(request, 'index.html') 







class MyProfile(LoginRequiredMixin, View):
        login_url = '/arkauth/login/'
        redirect_field_name = 'next'
        def get(self, request):
            user_form = UserUpdateForm(instance=request.user)
            profile_form = ProfileUpdateForm(instance=request.user.profile)
            
            context = { 
                'user_form': user_form,
                'profile_form': profile_form
            }
            
            return render(request, 'user/profile.html', context)
        
        def post(self,request):
            user_form = UserUpdateForm(
                request.POST, 
                instance=request.user
            )
            profile_form = ProfileUpdateForm(
                request.POST,
                request.FILES,
                instance=request.user.profile
            )

            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                
                messages.success(request,'Your profile has been updated successfully')
                
                return redirect('/profile/')
            else:
                context = {
                    'user_form': user_form,
                    'profile_form': profile_form
                }
                messages.error(request,'Error updating you profile')
                
                return render(request, 'user/profile.html', context)