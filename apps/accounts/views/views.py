from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from apps.accounts.forms import CustomUserRegistrationForm


def me(request):
    return redirect("/community/")


def user(request, username):
    return redirect("/community/")


def register_page(request):
    if request.user and request.user.is_authenticated:
        return redirect("community")
    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form = CustomUserRegistrationForm(request.POST)
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            print("mock save user")            
            return redirect("/community/")
            # user.save()
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
            return redirect("community")
        else:
            submitted_data = form.data.copy()
            form = CustomUserRegistrationForm(submitted_data)
            return render(request, 'accounts/registration.html', {'form': form})
    else:
        form = CustomUserRegistrationForm()
        return render(request, 'accounts/registration.html', {'form': form})
