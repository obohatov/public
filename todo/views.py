from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from todo.models import Task, Tag


class HomeView(View):
    def get(self, request):
        tasks = Task.objects.all().order_by("-is_done", "-created_at")
        return render(request, "todo/home.html", {"tasks": tasks})


class TagListView(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, "todo/tag_list.html", {"tags": tags})


class AddTaskView(View):
    def get(self, request):
        tags = Tag.objects.all()
        return render(request, "todo/add_task.html", {"tags": tags})

    def post(self, request):
        content = request.POST.get("content")
        deadline = request.POST.get("deadline")
        tags = request.POST.getlist("tags")
        task = Task.objects.create(content=content, deadline=deadline)
        task.tags.set(tags)
        return redirect("/")


class UpdateTaskView(View):
    def get(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        return render(request, "todo/update_task.html", {"task": task})

    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        content = request.POST.get("content")
        deadline = request.POST.get("deadline")
        tags = request.POST.getlist("tags")
        task.content = content
        task.deadline = deadline
        task.tags.set(tags)
        task.save()
        return redirect("/")

class DeleteTaskView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect("/")

class CompleteTaskView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.is_done = True
        task.save()
        return redirect("/")

class UndoTaskView(View):
    def post(self, request, task_id):
        task = get_object_or_404(Task, id=task_id)
        task.is_done = False
        task.save()
        return redirect("/")

class AddTagView(View):
    def get(self, request):
        return render(request, "todo/add_tag.html")

    def post(self, request):
        name = request.POST.get("name")
        Tag.objects.create(name=name)
        return redirect("/tags/")


class UpdateTagView(View):
    def get(self, request, tag_id):
        tag = get_object_or_404(Tag, id=tag_id)
        return render(request, "todo/update_tag.html", {"tag": tag})

    def post(self, request, tag_id):
        tag = get_object_or_404(Tag, id=tag_id)
        name = request.POST.get("name")
        tag.name = name
        tag.save()
        return redirect("/tags/")


class DeleteTagView(View):
    def post(self, request, tag_id):
        tag = get_object_or_404(Tag, id=tag_id)
        tag.delete()
        return redirect("/tags/")
