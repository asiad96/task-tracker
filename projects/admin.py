from django.contrib import admin
from .models import Project


# Register your models here.
@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ("name", "id")
