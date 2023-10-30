from arkauth import views
from django.urls import path

urlpatterns = [
  path("signup/",views.signup,name="signup"),
  path("login/",views.loginuser,name="login"),
  path("logout/",views.logoutuser,name="logout")
  
]
