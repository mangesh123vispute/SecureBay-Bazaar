
from django.urls import path,include
from arkapp import views
urlpatterns = [
    path('',views.home,name="index"),
    path('purchase/',views.purchase,name="purchase"),
    path('checkout/',views.checkout,name="checkout"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),
]
