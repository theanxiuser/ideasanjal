from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.


class IsUser(User):
    """
    ISUser model inherits User model. More fields are added,
    it is used as client login for first login part.
    """

    age = models.PositiveSmallIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, default="Not to say")
    profession = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    skills = models.TextField(null=True, blank=True)
    image = models.ImageField(default="unknown.jpg", upload_to="profile_image/")
    linkedin = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)

    # https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#django.contrib.auth.models.CustomUser.REQUIRED_FIELDS
    REQUIRED_FIELDS = ["first_name", "last_name", "username", "email", "password1", "password2"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    """ Post model for creating post by admin to show in home"""
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = RichTextUploadingField()
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(IsUser, on_delete=models.CASCADE)
    image = models.ImageField(default="", upload_to="post_img/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
