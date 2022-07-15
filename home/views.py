from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from home.forms import UserRegistrationForm, UserAuthenticationForm


def logout_view(request):
    """Logout user"""

    logout(request)
    messages.info(request, "You are logged out.")
    return redirect(reverse_lazy("home:home"))


def login_view(request):
    """If user is already login then redirect to feed page
    If request is POST then check if user is valid"""

    if request.user.is_authenticated:
        messages.info(request, "You are already logged in.")
        return redirect(reverse_lazy("home:home"))

    if request.method == "POST":
        form = UserAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.login(request)
            if user:
                login(request, user)
                messages.success(request, "Login successfully.")
                return redirect(reverse_lazy("home:home"))

    else:
        form = UserAuthenticationForm()

    return render(request, "registration/login.html", {"form": form})


def register(request):
    """If request is POST then check if user is valid for registration"""

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # display message to user
            messages.success(request, "Account created successfully!!")
            return redirect("home:login")

    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "registration/register.html", context)


class HomeView(View):
    """
    This is the home page of the website.
    """

    def get(self, request):
        return render(request, "home/control.html")
