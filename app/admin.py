from django.contrib import admin
from .models import Task,Emp

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=['task','user','emp','select']

@admin.register(Emp)
class EmpAdmin(admin.ModelAdmin):
    list_display=['name']