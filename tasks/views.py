from django.shortcuts import render
from .models import Task


def task_list(request):
    vazifa_nomi = request.GET.get('vazifa_nomi')
    vazifa_tafsifi = request.GET.get('vazifa_tafsifi')
    status = request.GET.get('status')
    if vazifa_nomi and vazifa_tafsifi and status:
        Task.objects.create(
            vazifa_nomi = vazifa_nomi,
            vazifa_tafsifi = vazifa_tafsifi,
            status = status
        )
    tasks = Task.objects.all()
    ctx = {'tasks': tasks}
    return render(request, 'tasks/task-list.html', ctx)