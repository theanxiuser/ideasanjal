from django.urls import path
from . import views

# including urlpatterns
from .views import PostDetailView

app_name = "home"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),

    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    path("i/", views.ProfileView.as_view(), name="profile"),
    path("i/edit/", views.EditProfileView.as_view(), name="edit_profile"),

    path("<str:slug>/", PostDetailView.as_view(), name="post_detail"),
]
