from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView

from home.forms import UserRegistrationForm, UserAuthenticationForm, BlogSubmitForm
from home.models import IsUser, Post


def blog_submit(request):
    """View for posting blog to the admin"""
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BlogSubmitForm(request.POST, request.FILES)

            if form.is_valid():
                obj = form.save(commit=False)
                obj.author = IsUser.objects.get(pk=request.user.id)
                obj.save()
                messages.success(request, "Blog post is submitted. Wait for admin approval.")
                return redirect("home:home")

        else:
            form = BlogSubmitForm()
        context = {"blog": form}
        return render(request, "home/blog_submit.html", context)
    else:
        return redirect("home:login")


class PostDetailView(LoginRequiredMixin, DetailView):
    """Detail of post"""
    model = Post
    template_name = "home/post_detail.html"


class EditProfileView(LoginRequiredMixin, UpdateView):
    """Edit own profile"""

    # form = EditProfileForm
    model = IsUser
    fields = ["image", "first_name", "last_name", "email", "age", "gender", "profession", "bio", "skills", "linkedin", "twitter",
              "facebook", "github"]
    template_name = "home/edit_profile.html"
    success_url = reverse_lazy("home:profile")

    def get_object(self):
        return get_object_or_404(IsUser, pk=self.request.user.id)


class ProfileView(DetailView):
    """Profile view is used to display own profile"""

    template_name = "home/profile.html"
    context_object_name = "user"

    def get_object(self):
        return get_object_or_404(IsUser, id=self.request.user.id)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context["self_profile"] = True
        return context


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
        if request.user.is_authenticated:
            queryset = Post.objects.filter(status=1).order_by('-created_at')
            ctx = {"post_list": queryset}
            return render(request, "home/feed.html", ctx)

        return render(request, "home/home.html")

