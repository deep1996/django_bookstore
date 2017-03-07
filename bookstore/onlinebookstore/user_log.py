from django import forms

class logged(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)




