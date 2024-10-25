from django import forms

class InputForm(forms.Form):
    text: str = forms.CharField(max_length=2000)