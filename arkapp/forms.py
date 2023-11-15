
from .models import Profile
from django import forms
from django.contrib.auth.models import User
 
# create a ModelForm
class UserUpdateForm(forms.ModelForm):
   
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
   
    class Meta:
        model = Profile
        fields = "__all__"