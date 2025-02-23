
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView

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
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
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
                return redirect('product_list')

        else:
            form = RegisterForm()
        context = {
            'form': form
        }
        return render(request, 'accounts/register.html', context)

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        email = form.cleaned_data['email']
        send_mail(email,'Succesfully registered','diyorbekramonovich02s@gmail.com',[email],fail_silently=False)
        user.backend = 'social_core.backends.google.GoogleOAuth2'
        login(self.request, user)
        return redirect(self.success_url)
