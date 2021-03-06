from django import forms
from django.contrib.auth.models import User

class JoinForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField()
    
