from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    try:
        tasks = Task.objects.all().order_by('-created')

    except:
        tasks = ''
    Task.objects.order_by('-created')
    ordering = ['-created']
    context = {
        'tasks': tasks,
    }

    return render(request, 'backend/index.html', context)

def add(request):
    if request.method == "POST":
        if request.POST['content'] != '' and len(request.POST['content']) < 30:
            new = Task(task=request.POST['content'])
            new.save()
    return HttpResponseRedirect('/')

def delete(request):
    if request.method == "POST":
        obj = Task.objects.get(id=request.POST['task-id'])
        obj.delete()
    return HttpResponseRedirect('/')