
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render

from accounts.forms import LoginForm, RegisterForm


def login_page(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                return redirect('product_list')
            else:
                messages.add_message(request,messages.ERROR,'Email or password is incorrect')

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('product_list')

def register_view(request):
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(user.password)
                user.save()
                login(request, user)
                return redirect('product_list')

        else:
            form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)
