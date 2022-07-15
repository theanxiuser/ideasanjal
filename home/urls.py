from django.urls import path
from . import views

# including urlpatterns

app_name = "home"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),

    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
