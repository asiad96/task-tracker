from django.shortcuts import render, get_object_or_404
from .models import Project
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def list_projects(request):
    list_projects = Project.objects.filter(owner=request.user)
    context = {
        "list_projects": list_projects,
    }
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project_object": project,
    }
    return render(request, "projects/detail.html", context)
