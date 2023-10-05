from django.shortcuts import render, redirect, get_object_or_404
from todo.models import Task, Tag


def home(request):
    tasks = Task.objects.all().order_by("-is_done", "-created_at")
    return render(request, "todo/home.html", {"tasks": tasks})


def tag_list(request):
    tags = Tag.objects.all()
    return render(request, "todo/tag_list.html", {"tags": tags})


def add_task(request):
    if request.method == "POST":
        content = request.POST.get("content")
        deadline = request.POST.get("deadline")
        tags = request.POST.getlist("tags")
        task = Task.objects.create(content=content, deadline=deadline)
        task.tags.set(tags)
        return redirect("/")
    return render(request, "todo/add_task.html")


def update_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        content = request.POST.get("content")
        deadline = request.POST.get("deadline")
        tags = request.POST.getlist("tags")
        task.content = content
        task.deadline = deadline
        task.tags.set(tags)
        task.save()
        return redirect("/")
    return render(request, "todo/update_task.html", {"task": task})


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("/")


def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_done = True
    task.save()
    return redirect("/")


def undo_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_done = False
    task.save()
    return redirect("/")


def add_tag(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Tag.objects.create(name=name)
        return redirect("/tags/")
    return render(request, "todo/add_tag.html")


def update_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    if request.method == "POST":
        name = request.POST.get("name")
        tag.name = name
        tag.save()
        return redirect("/tags/")
    return render(request, "todo/update_tag.html", {"tag": tag})


def delete_tag(request, tag_id):
    tag = get_object_or_404(Tag, id=tag_id)
    tag.delete()
    return redirect("/tags/")
