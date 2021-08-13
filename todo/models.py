from django.db import models

# Create your models here.
class TodoItem(models.Model): #Creates a class called todoitem which represents each data item in our database
    content= models.TextField()
