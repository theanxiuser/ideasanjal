from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from home.forms import UserRegistrationForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # display message to user
            messages.success(request, "Account created successfully!!")
            return redirect("login")

    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "registration/register.html", context)


class HomeView(View):
    """
    This is the home page of the website.
    """

    def get(self, request):
        return render(request, "home/index.html")
