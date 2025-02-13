from django import forms

from accounts.models import User


class LoginForm(forms.Form):
    email = forms.CharField(max_length=100,label='email')
    password = forms.CharField(widget=forms.PasswordInput,label='password')




class RegisterForm(forms.ModelForm):
    email = forms.CharField(max_length=100,label='email')
    password = forms.CharField(widget=forms.PasswordInput,label='password')
    confirm_password = forms.CharField(widget=forms.PasswordInput,label='confirm_password')
    username = forms.CharField(max_length=100,label='username',required=False)

    class Meta:
        model = User
        fields = ('email','password','confirm_password','username')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = self.data.get('password')
        confirm_password = self.data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data
