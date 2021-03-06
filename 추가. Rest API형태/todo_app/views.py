from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .api import TodoSerializer
from .forms import TodoForm  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json


# Create your views here.
@api_view(['GET'])
def index(request):
    todos = Todo.objects.all().order_by("schedule")
    serializer=TodoSerializer(todos,many=True)
    return Response(serializer.data)

    # if request.method =="POST":
    #     if request.POST["1"]=='서울':
    #         todos = Todo.objects.filter(city="서울").order_by("schedule")
    #         context={'todos':todos}
    #         return render(request,'todo_app/index.html',context)
    #     elif request.POST["1"]=='경기':
    #         todos = Todo.objects.filter(city="경기").order_by("schedule")
    #         context={'todos':todos}
    #         return render(request,'todo_app/index.html',context)
    #     elif request.POST["1"]=='인천':
    #         todos = Todo.objects.filter(city="인천").order_by("schedule")
    #         context={'todos':todos}
    #         return render(request,'todo_app/index.html',context)
    #     elif request.POST["1"]=='대전·충청':
    #         todos = Todo.objects.filter(city="대전,충청").order_by("schedule")
    #         context={'todos':todos}
    #         return render(request,'todo_app/index.html',context)
    #     elif request.POST["1"]=='대구·경북':
    #         todos = Todo.objects.filter(city="대구,경북").order_by("schedule")
    #         context={'todos':todos}
    #         return render(request,'todo_app/index.html',context)
    #     elif request.POST["1"]=='부산':
    #         todos = Todo.objects.filter(city="부산").order_by("schedule")
    #         context={'todos':todos}
    #         return render(request,'todo_app/index.html',context)
    #     elif request.POST["1"]=='울산':
    #         todos = Todo.objects.filter(city="울산")
    #         context={'todos':todos}
    #         return render(request,'todo_app/index.html',context)
    #     elif request.POST["1"]=='광주':
    #         todos = Todo.objects.filter(city="광주").order_by("schedule")
    #         context={'todos':todos}
    #         return render(request,'todo_app/index.html',context)
    #     else: 
    #         todos = Todo.objects.all().order_by("schedule")
    #         context={'todos':todos}
    #         return render(request,'todo_app/index.html',context)
    # context={'todos':todos}
    # return render(request,'todo_app/index.html',context)


    
    

# 내용 상세 페이지
@api_view(['GET'])
def detailTodo(request, todo_id):
    todo=Todo.objects.get(id=todo_id)
    serializer=TodoSerializer(todo)
    return Response(serializer.data)

    # todo = get_object_or_404(Todo, pk=todo_id)
    # return render(request, 'todo_app/detail.html', {'todo': todo})


# 새로운 글 등록
@api_view(['POST'])
def createTodo(request):
    serializer=TodoSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

    # if request.method == 'POST':
    #     form = TodoForm(request.POST)
    #     if form.is_valid():
    #         form=form.save(commit=False)
    #         form.user=request.user
    #         form.save()
    #         return redirect('index')
        
    # else:
    #     form = TodoForm()
    # return render(request, 'todo_app/create.html', {'form': form})

# 글 수정
@api_view(['PUT'])
def updateTodo(request, todo_id):
    todo=Todo.objects.get(id=todo_id)
    serializer=TodoSerializer(instance=todo,data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)
    # todo = get_object_or_404(Todo, pk=todo_id)
    # if str(request.user) == str(todo.user):
    #     if request.method == 'POST':
    #         form = TodoForm(request.POST, instance=todo)
    #         if form.is_valid():
    #             form.save()
    #             return redirect('detailTodo', todo_id)
        
    #     else:
    #         form = TodoForm(instance=todo)
    # else:
    #     messages.warning(request, '본인 글만 수정 가능합니다.')
    #     return redirect('detailTodo', todo_id)
        
    
    # return render(request, 'todo_app/update.html', {'form': form})


# 글 삭제
@api_view(['DELETE'])
def deleteTodo(request, todo_id):
    todo=Todo.objects.get(id=todo_id)
    todo.delete()
    return Response('Deleted!! ')
    # todo = get_object_or_404(Todo, pk=todo_id)

    # if str(request.user) == str(todo.user):
    #     todo = Todo.objects.get(pk=todo_id)
    #     todo.delete()
    #     return redirect('index')
    # else:
    #     messages.warning(request, '본인 글만 삭제 가능합니다.')
    #     return redirect('detailTodo', todo_id)


@api_view(['PPST'])
def applyTodo(request):
    pk = request.POST.get('pk', None)
    todo=Todo.objects.get(id=pk)
    # pk = request.POST.get('pk', None)
    # todo = get_object_or_404(Todo, pk=pk)
    # user = request.user

    # if todo.apply.filter(id=user.id).exists():
    #     todo.apply.remove(user)
    #     message = '신청 취소'
    # else:
    #     todo.apply.add(user)
    #     message = '신청 완료'

    # context = {'apply_count':todo.count_apply_user(), 'message': message}
    # return HttpResponse(json.dumps(context), content_type="application/json")