from django.db import models
# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.TextField()
    category = models.CharField(max_length=200)
    date =models.DateField()

    def __str__(self) ->str:
        return self.name
    


class comment(models.Model):
    
    koment = models.TextField()
    name = models.CharField(max_length=30)
    mark =models.IntegerField()

    def __str__(self) ->str:
        return self.name


class maxsulot(models.Model):    
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    discription= models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self) ->str:
        return self.title