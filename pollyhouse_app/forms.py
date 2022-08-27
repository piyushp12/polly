import email
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=10, min_length=10)