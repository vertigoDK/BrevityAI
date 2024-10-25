from django.shortcuts import render
from .services.site_summarizer import SiteSummarizer
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.decorators import login_required
from .forms import SiteUrlForms

@login_required
def site_summarizer_view(request: HttpRequest) -> HttpResponse:
    
    if request.method == 'POST':
        form = SiteUrlForms(request.POST)
        
        if form.is_valid():
            print('форма валидна')
            site_url = form.cleaned_data['site_url']

            siteSummarizer: SiteSummarizer = SiteSummarizer()
            
            response: dict[str, str] = siteSummarizer.summarize_site(link=site_url)
            
            print(response)
            
            return render(request=request, template_name="site_summarizer/site_summarizer.html", context={'response': response})
        else:
            print('Форма не валидна')
            print(form.errors)
    else:
        form = SiteUrlForms()
        
    return render(request=request, template_name="site_summarizer/site_summarizer.html")