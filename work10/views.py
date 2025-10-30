from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Todo
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # ← さっき作ったテンプレートを使う
    success_url = reverse_lazy('todo_list')    # ← ログイン後に行くページ（後で変更可）

@login_required
def todo_list(request):
    todos = Todo.objects.all().order_by('-created_at')
    return render(request, 'work10/todo_list.html', {'todos': todos})

@login_required
def add_todo(request):
    if request.method == 'POST':
        task = request.POST['task']
        Todo.objects.create(user=request.user, task=task)
        return redirect('todo_list')
    return render(request, 'work10/add_todo.html')

@login_required
def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if todo.user == request.user:  # 自分のタスクだけ削除可
        todo.delete()
    return redirect('todo_list')
