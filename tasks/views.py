from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the task management system")

def contact(request):
    return HttpResponse("this is the contact")
    
def show_task(request):
    return HttpResponse("this is the show_task")

def show_task_specific_work(request,id):
    print("id",id)
    print("id type",type(id))
    return HttpResponse("this is the my specific show_task")