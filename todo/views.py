from django.shortcuts import render, redirect
from todo.models import Task, Tag


def home(request):
    tasks = Task.objects.all().order_by("-is_done", "-created_at")
    return render(request, "home.html", {"tasks": tasks})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "tag_list.html", {"tags": tags})


def add_task(request):
    if request.method == "POST":
        content = request.POST.get("content")
        deadline = request.POST.get("deadline")
        tags = request.POST.getlist("tags")
        task = Task.objects.create(content=content, deadline=deadline)
        task.tags.set(tags)
        return redirect("/")
    return render(request, "add_task.html")


def add_tag(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Tag.objects.create(name=name)
        return redirect("/tags/")
    return render(request, "add_tag.html")
