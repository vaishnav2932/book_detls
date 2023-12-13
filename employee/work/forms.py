from django import forms
from work.models import Book,student


class EmpForm(forms.Form):
    email=forms.EmailField()
    uname=forms.CharField()
    age=forms.CharField()
    place=forms.CharField()

class BookForm(forms.ModelForm):

    class Meta:
        model=Book
        fields='__all__'


