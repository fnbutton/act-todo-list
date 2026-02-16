from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TaskList

def index(request):

    if request.method == 'POST':
        print(request)
        try:
            name=request.POST.get('name')

            task_list = TaskList(name=name)
            task_list.save()
        except Exception as e:
            # TODO error al gener un nuevo TaskList
            print(e)

        return redirect('index')
    
    try:
        task_lists = TaskList.objects.order_by('-created_at')
    except Exception as e:
        # TODO error al listar objetos
        print(e)
    
    return render(request, 'tasklist/index.html', context={'listas': task_lists})
    

def delete_tasklist(request, id_list):
    if request.method == 'DELETE':
        try:
            task_list = TaskList.objects.get(pk=id_list)
            task_list.delete()
        except Exception as e:
            # TODO: implementar el error al eliminar
            print(e)
    else:
        return redirect(f'/lists/{id_list}/tasks')

    return  HttpResponse('')