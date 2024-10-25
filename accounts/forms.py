from django import forms
from django.contrib.auth.models import User


class CustomLoginForm(forms.Form):
    login = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput())    


class CustonUserRegistrationForm(forms.Form):
    login = forms.CharField(max_length=32)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Passwords do not match.")
            
            
    def clean_login(self):
        login = self.cleaned_data["login"]
        if User.objects.filter(username=login).exists():
            raise forms.ValidationError("Username already exists.")
        return login