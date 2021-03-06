from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User
from .forms import TodoForm

def index(request):
    return redirect('todos:home')

def home(request):
    form = TodoForm()
    if request.user.is_authenticated:
        todos = request.user.todo_set.all()  # 현재 유저가 가지고 있는 todo 들
        context = {
            'todos': todos,
            'form':form,
        }
    else:
        context = {}
    return render(request, 'todos/home.html', context)
    # if request.user.is_authenticated:
    #     # todos = T`odo.objects.filter(user_id=request.user).order_by('completed', '-id')
    #     todos = request.user.todo_set.order_by('completed', '-id')
    #     return render(request, 'todos/home.html', {
    #         'todos': todos
    #     })
    # else:
    #     todos = None
    #     return render(request, 'todos/home.html', {
    #         'todos': todos
    #     })

def create(request):
    # todos 작성하기
    Todo.objects.create(content=request.POST.get('content'), user_id=request.user.id)
    return redirect('todos:home')
# def create(request):
#     # todos 작성하기
#     # Todo.objects.create(content=request.POST.get('content'), user_id=request.user.id)
#     user = request.user
#     todo = Todo(user=user)
#     form = TodoForm(request.POST, instance=todo)
#     if form.is_valid():
#         form.save()
#     return redirect('todos:home')

def check(request, todo_id):
    # 특정 id를 가진 TODO를 뽑아 Completed = True
    todo = Todo.objects.get(id=todo_id)
    if todo.completed:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('todos:home')

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect('todos:home')
