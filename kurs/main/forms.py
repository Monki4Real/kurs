from django import forms
from .models import News, Cheatsheet

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class CheatsheetForm(forms.ModelForm):
    class Meta:
        model = Cheatsheet
        fields = '__all__'