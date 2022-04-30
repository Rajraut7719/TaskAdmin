from django.shortcuts import render
from .models import Task
from app import models
# Create your views here.
def index(request):
    task=Task.objects.all()
    return render(request,'app/index.html',{'tasks':task})