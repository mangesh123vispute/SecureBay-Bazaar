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
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
# emails
from django.core.mail import send_mail,EmailMultiAlternatives
from django.core.mail import BadHeaderError ,send_mail
from ecommerse.manage import main
from django.core import mail
from django.conf import settings
from django.contrib import messages


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

        messages.info(request,"Signup Successful ! Please enter login")
        return redirect('/arkauth/login/')

    return render(request,"auth/signup.html")


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
