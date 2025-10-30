from django.shortcuts import render
from .models import Todo
from datetime import date



def todo_list(request):
    todos = Todo.objects.all().order_by('due_date')
    today = date.today()
    return render(request, 'work09/todo_list.html', {'todos': todos, 'today': today})

from django.shortcuts import redirect
from datetime import datetime


def todo_create(request):
    if request.method == "POST":
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        Todo.objects.create(title=title, due_date=due_date)
    return redirect('todo_list')

from django.shortcuts import get_object_or_404
def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "POST":
        if 'update' in request.POST:
            todo.title = request.POST.get('title')
            todo.due_date = request.POST.get('due_date')
            todo.is_completed = 'is_completed' in request.POST
            todo.save()
        elif 'delete' in request.POST:
            todo.delete()
        return redirect('todo_list')
    return render(request, 'work09/todo_edit.html', {'todo': todo})

from django.http import HttpResponse

def index(request):
    return HttpResponse("✅ work09 TODOアプリのトップページです！")

def index(request):
    todos = Todo.objects.all().order_by('due_date')  # 期限日順で取得
   # sort_key = request.GET.get('sort', 'due_date')
    #todos = Todo.objects.all().order_by(sort_key)
    return render(request, 'work09/index.html', {'todos': todos})