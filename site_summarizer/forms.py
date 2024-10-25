from django import forms
from .services.site_summarizer import SiteSummarizerTools

class SiteUrlForms(forms.Form):
    site_url = forms.URLField(required=True, label="Site Url")
    
