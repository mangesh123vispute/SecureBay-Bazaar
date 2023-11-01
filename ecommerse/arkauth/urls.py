from arkauth import views
from django.urls import path

urlpatterns = [
  path("signup/",views.signup,name="signup"),
  path("login/",views.loginuser,name="login"),
  path("logout/",views.logoutuser,name="logout"),
  path('activate/<uidb64>/<token>',views.ActivateAccountView.as_view(),name="activate"),
  path('request-reset-email/',views.RequestResetEmailView.as_view(),name="request-reset-email"),  
  path('set-new-password/<uidb64>/<token>/', views.SetNewPasswordView.as_view(), name='set-new-password'),

]
