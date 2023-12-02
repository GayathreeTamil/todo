from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Task

# Create your views here.
def addTask(req):
    task = req.POST['task']
    Task.objects.create(task = task)
    # return HttpResponse('The form is submitted')
    return redirect('home')
def markAsDone(req, pk):
    # return HttpResponse(pk)
    task = get_object_or_404(Task, id=pk)
    task.is_completed = True
    task.save()
    return redirect('home')
    # return HttpResponse(task)
def markAsUndone(req, pk):
    task = get_object_or_404(Task, id=pk)
    task.is_completed = False
    task.save()
    return redirect('home')
def editTask(req, pk):
    task = get_object_or_404(Task, id = pk)
    if req.method == 'POST':
        new_task = req.POST['task']
        print(new_task)
        task.task = new_task
        task.save()
        return redirect('home')
    else:
        context = {
            'get_task': task
        }
        return render(req, 'editTask.html', context)
def deleteTask(req, pk):
    task = get_object_or_404(Task, id = pk)
    task.delete()
    return redirect('home')
