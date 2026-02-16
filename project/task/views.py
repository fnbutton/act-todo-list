import json
from django.http import QueryDict
from django.shortcuts import render, redirect
from .models import Task, TaskList

def index(request, id_list):
    try:
        task_list = TaskList.objects.get(pk=id_list)
    except Exception as e:
        print(e)
        return redirect('/lists')

    if request.method == 'POST':
        try:
            title = request.POST['title']
            task = Task(title=title)
            task.task_list = TaskList.objects.get(pk=id_list)
            task.save()
        except Exception as e:
            # TODO error al guardar objetos
            print(e)

        return redirect(f'/lists/{id_list}/tasks')

    try:
        tasks = Task.objects.filter(task_list=id_list).order_by('-created_at')
        for t in tasks:
            print(t.complated)
    except Exception as e:
        # TODO error al listar objetos
        print(e)

    return render(request, 'task/index.html', context={'l': task_list, 'tasks': tasks})

def modify(request, id_list, id_task):

    if request.method == 'DELETE':
        try:
            task = Task.objects.get(pk=id_task)
            task.delete()
        except Exception as e:
            # TODO error al guardar objetos
            print(e)

        return redirect(f'/lists/{id_list}/tasks')

    if request.method == 'PATCH':
        try:

            body = json.loads(request.body.decode('utf-8'))
            status = body['status']

            task = Task.objects.get(pk=id_task)
            task.complated = status
            
            task.save()

            

        except Exception as e:
            # TODO error al guardar objetos
            print(e)

        return redirect(f'/lists/{id_list}/tasks')


    