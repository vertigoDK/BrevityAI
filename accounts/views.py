from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import CustomLoginForm, CustonUserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def logout_view(request: HttpRequest) -> HttpResponse:
    
    if request.user.is_authenticated:
        logout(request=request)
        
    return redirect('home')


def login_view(request: HttpRequest) -> HttpResponse:
    
    if not request.user.is_authenticated:
        
        errors: list[str] = []
        
        if request.method == 'POST':
            form = CustomLoginForm(request.POST)
            
            if form.is_valid():
                user_login = form.cleaned_data['login']
                user_password = form.cleaned_data['password']
                
                user = authenticate(username=user_login, password=user_password)
                
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    errors.append('Ошибка при поптыке входа в сервис')
                
                
        else:
            form = CustomLoginForm()
        
        return render(request, 'accounts/login_page.html')
    else:
        return redirect('home')
    
    
def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CustonUserRegistrationForm(request.POST)
        
        if form.is_valid():
            user_login: str = form.cleaned_data['login']
            user_password: str = form.cleaned_data['password1']
            
            user = User(username=user_login)
            user.set_password(user_password)
            user.save()
            
            return redirect('login')
            
    else:
        form = CustonUserRegistrationForm()
        
    return render(request=request, template_name='accounts/register_page.html')