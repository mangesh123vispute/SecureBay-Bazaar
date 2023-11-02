
from django.urls import path,include
from arkapp import views
urlpatterns = [
    path('',views.home,name="index"),
    path('purchase/',views.purchase,name="purchase"),
]
