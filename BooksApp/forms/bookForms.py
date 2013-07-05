__author__ = 'OMID EBRAHIMI'

from django import forms

class SearchForm(forms.Form):
    title = forms.CharField(required=True, max_length=100)