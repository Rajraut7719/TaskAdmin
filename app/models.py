
from django.db import models
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField
# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

SELECT_CHOICES = (
    ("Pending", "Pending"),
    ("Done", "Done"),
    ("Error in task", "Error in task"),
   
)
class Task(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    emp=models.ForeignKey(Emp,on_delete=models.CASCADE)
    select= models.CharField(max_length = 20,choices = SELECT_CHOICES,default='')
    task=models.TextField(blank='r')


