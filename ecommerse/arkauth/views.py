
import arkapp
import django.db
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,logout,login
import django.contrib
from django.contrib.auth.models import User
# to activate the user account
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.urls import NoReverseMatch,reverse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
# emails
from django.core.mail import send_mail,EmailMultiAlternatives,EmailMessage
from django.core.mail import BadHeaderError ,send_mail

from django.core import mail
from django.conf import settings    
from django.contrib import messages
from ecommerse.settings import EMAIL_HOST, EMAIL_HOST_USER
from .utils import TokenGenerator,generate_token
from django.views.generic import View
import threading
# threading

class EmailThread(threading.Thread):
    def __init__(self,email_message):
        self.email_message=email_message
    def run(self):
        self.email_message.send()

# Create your views here.
def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        conform_password=request.POST['password2']
        if password!=conform_password:
            messages.warning(request,"Password is not Matching!")
            return render(request,"auth/signup.html")
        
        try:
            if User.objects.get(username=email):
                messages.warning(request,"Email is already taken")
                return render(request,"auth/signup.html")
        except:
            pass
        user =User.objects.create_user(email ,email,password)
        user.is_active=False
        user.save()
        current_site=get_current_site(request)
        email_subject="Activate your Account"   
        message=render_to_string('auth/activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)

        })

        email_message = EmailMultiAlternatives(email_subject, message, settings.EMAIL_HOST_USER, [email])
        email_message.send()

        messages.info(request, "Activate Your account by clicking link on your email")
        return redirect("/arkauth/login/")

    return render(request, "auth/signup.html")


def loginuser(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['password']
        myuser=authenticate(request,username=username,password=password)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login in success")
            return render(request,"index.html")
        else:
            messages.error(request,"Invalid creadiantials")
            return redirect("/arkauth/login/")
    
    return render(request,"auth/login.html")

def logoutuser(request):
    logout(request)
    messages.success(request,"logout user!")
    return redirect("/arkauth/login/")


class ActivateAccountView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if generate_token.check_token(user, token):  # Make sure you have a valid check_token function
                user.is_active = True
                user.save()
                messages.success(request, "Account Activated Successfully")
                return redirect('/arkauth/login/')
            else:
                messages.error(request, "Invalid activation token")
                return render(request, "auth/activatefail.html")
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            messages.error(request, "Invalid activation link")
            return render(request, "auth/activatefail.html")