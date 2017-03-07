from django import forms

class userform(forms.Form):
    username=forms.CharField(max_length=20,min_length=5)
    first_name=forms.CharField(label='First name')
    last_name=forms.CharField(label='Last name')
    email=forms.EmailField()
    password=forms.CharField(min_length=5, widget=forms.PasswordInput)




