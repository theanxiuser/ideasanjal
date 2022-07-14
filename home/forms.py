from django import forms
from django.contrib.auth.forms import UserCreationForm

from home.models import IsUser


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
