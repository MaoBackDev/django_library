from django import forms

from apps.books.models import Book
from .models import *


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ('book', 'reader',)


class LoanMultipleForm(forms.ModelForm):

    books = forms.ModelMultipleChoiceField(
        queryset = None,
        required = True,
        widget = forms.CheckboxSelectMultiple,   
    )

    class Meta:
        model = Loan
        fields = ('reader',)

    def __init__(self, *args, **kwargs):
        super(LoanMultipleForm, self).__init__(*args, **kwargs)
        self.fields['books'].queryset=Book.objects.all() 
        
