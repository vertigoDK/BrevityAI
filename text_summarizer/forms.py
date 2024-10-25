from django import forms

class TextSummarizerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label="Enter text to summarize", max_length=2000)