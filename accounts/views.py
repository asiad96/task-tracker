from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User


# Create your views here.
def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("list_projects")
    else:
        form = LoginForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confrimation = form.cleaned_data["password"]

            if password == password_confrimation:
                user = User.objects.create_user(username, password=password)

                login(request, user)

                return redirect("list_projects")
            else:
                form.add_error("password", "the passwords do not match")
    else:
        form = SignUpForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/signup.html", context)
