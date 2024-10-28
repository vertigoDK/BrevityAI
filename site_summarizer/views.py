from django.shortcuts import render, redirect
from .services.site_summarizer import SiteSummarizer
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from .forms import SiteUrlForms
from django.contrib import messages

@login_required
def site_summarizer_view(request: HttpRequest) -> HttpResponse:
    
    if request.method == 'POST':
        form = SiteUrlForms(request.POST)
        
        if form.is_valid():
            site_url = form.cleaned_data['site_url']

            siteSummarizer: SiteSummarizer = SiteSummarizer()
            
            response: dict[str, str] = siteSummarizer.summarize_site(link=site_url)
            
            request.session['response'] = response
            
            return redirect('site-summarizer')
        else:
            print(form.errors)
    else:
        form = SiteUrlForms()
    
    response = request.session.pop('response', None)
    
    return render(request=request, template_name="site_summarizer/site_summarizer.html", context={'form': form, 'response': response})