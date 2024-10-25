from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import TextSummarizerForm
from .services.text_summarizer import TextSummarizer
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

@login_required
def text_summarizer(request: HttpRequest) -> HttpResponse:
    
    text_summarizer = TextSummarizer()
    
    if request.method == "POST":
        form = TextSummarizerForm(request.POST)
        
        
        if form.is_valid():
            
            text_to_summarize: str = form.cleaned_data['text'] 
            summarized_data: dict[str, str] = text_summarizer.text_summarize(text_to_summarize=text_to_summarize)
            
            request.session['summarized_data'] = summarized_data
            
            return redirect('text-summarizer')

    else:
        form = TextSummarizerForm()  

    summarized_data = request.session.pop('summarized_data', None)

    return render(request, 'text_summarizer/text_summarizer.html', {
        'summarized_data': summarized_data,
    })

