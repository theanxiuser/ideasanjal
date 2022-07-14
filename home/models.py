from django.db import models
from django.contrib.auth.models import User

# Create your models here.

GENDER = (
    (0, "Female"),
    (1, "Male"),
    (2, "Other"),
    (3, "Not to say")
)


class IsUser (models.Model):
    """
    ISUser model uses User model. More fields are added,
    it is used as client login for first login part.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(null=False)
    gender = models.IntegerField(GENDER, default=3)
    profession = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    skills = models.TextField(null=True, blank=True)
    image = models.ImageField(default="/media/profile_image/unknown.jpg", upload_to="profile_image/")
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    