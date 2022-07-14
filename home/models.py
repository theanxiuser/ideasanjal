from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER = (
    (0, "Female"),
    (1, "Male"),
    (2, "Other"),
    (3, "Not to say")
)


class IsUser (User):
    """
    ISUser model inherits User model. More fields are added,
    it is used as client login for first login part.
    """

    age = models.PositiveSmallIntegerField(null=True, blank=True)
    gender = models.IntegerField(GENDER, default=3)
    profession = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    skills = models.TextField(null=True, blank=True)
    image = models.ImageField(default="/media/profile_image/unknown.jpg", upload_to="profile_image/")
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)

    # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "email", "password1", "password2"]

    def __str__(self):
        return self.username
