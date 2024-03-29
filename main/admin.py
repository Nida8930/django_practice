from django.contrib import admin
from .models import Tutorial
from tinymce.widgets import TinyMCE
from django.db import models


# Register your models here.

class Tutorialadmin(admin.ModelAdmin):
    #fields = ["tutorial_title",
    #         "tutorial_published",
    #         "tutorial_content"]

    fieldsets = [
        ("Title/Date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields": ["tutorial_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Tutorial, Tutorialadmin)
