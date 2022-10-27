from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.
from django.db import models
from .models import Post, IsUser


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status")
    list_filter = ("status",)
    search_fields = ("title", "content")
    formfield_overrides = {
        models.TextField: {'widget':
                               CKEditorUploadingWidget()}
    }


admin.site.register(Post, PostAdmin)
admin.site.register(IsUser)
