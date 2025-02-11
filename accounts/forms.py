from django import forms

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100,label='email')
    password = forms.CharField(widget=forms.PasswordInput,label='password')



