from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .forms import InputForm
from services.base_summarizator.summarizator import Summarizer



def home(request: HttpRequest) -> HttpResponse:
    
    if request.method == 'POST':
        
        if request.user.is_authenticated:
            
            form = InputForm(request.POST)

            if form.is_valid():
                text_for_summary: str = form.cleaned_data['text']
                
                request.session['text'] = text_for_summary
        else:
            redirect('login')
            
    return render(request=request, template_name='core/home.html')

def summarizers_list(request: HttpRequest) -> HttpResponse:
    
    return render(request=request, template_name='core/summarizers_list.html') # Добавить остальные аргументы