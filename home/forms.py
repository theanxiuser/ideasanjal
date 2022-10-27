from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from home.models import IsUser, Post
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class BlogSubmitForm(forms.ModelForm):
    """Form for post creation bt the users"""
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ["title", "slug", "content", "image"]


class UserAuthenticationForm(forms.Form):
    username = forms.CharField(label="Username", max_length=20, min_length=5,
                               widget=forms.TextInput(attrs={"placeholder": "Username"}))

    password = forms.CharField(label="Password", max_length=30,
                               widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

    def clean(self):
        """Check if user is valid."""

        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid username or password.")
        return self.cleaned_data

    def login(self, request):
        """Login a user."""
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        return user


class UserRegistrationForm(UserCreationForm):
    """
    This is the form for user registration.
    """
    # https://stackoverflow.com/questions/8466851/making-first-name-last-name-a-required-attribute-rather-than-an-optional-one-in
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        """
        This is the meta class for the form.
        """
        model = IsUser
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

    # def __init__(self, *args, **kwargs):
    #     """
    #     This is the init function for the form.
    #     """
    #
    #     super(UserRegistrationForm, self).__init__(*args, **kwargs)
    #     self.fields["username"].label = "Username"
    #     self.fields["email"].label = "Email"
    #     self.fields["password1"].label = "Password"
    #     self.fields["password2"].label = "Confirm Password"
