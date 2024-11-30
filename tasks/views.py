from django.shortcuts import render
from .models import Task


def task_list(request):
    title = request.GET.get('title')
    description = request.GET.get('description')
    is_completed = request.GET.get('is_completed')
    print(title, description, is_completed)
    if title and description:
        is_completed = True if is_completed == "on" else False
        Task.objects.create(
            title=title,
            description=description,
            is_completed=is_completed
        )
    tasks = Task.objects.all()
    ctx = {'tasks': tasks}
    return render(request, 'tasks/task-list.html', ctx)
