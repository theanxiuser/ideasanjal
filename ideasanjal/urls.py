"""ideasanjal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include, re_path

import home
from ideasanjal import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls")),
    # url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

# https://stackoverflow.com/questions/42856793/django-is-not-displaying-the-image-via-media
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
