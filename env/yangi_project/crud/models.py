from django.db import models

# Create your models here.
class Todo(models.Model):
     title=models.TextField()
     discription=models.TextField()

     def __str__(self):
         return self.title
     