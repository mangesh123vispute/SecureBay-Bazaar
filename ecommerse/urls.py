"""
URL configuration for ecommerse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import django.conf
from django.contrib import admin
from django.urls import path,include
from arkauth.views import signup
from django.conf import settings
from django.conf.urls.static import static
from ecommerse.ecommerse.settings import STATIC_URL

admin.site.site_header="SecureBuy"
admin.site.site_title="ARK admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('arkapp.urls')),
    path('arkauth/',include('arkauth.urls')),
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)