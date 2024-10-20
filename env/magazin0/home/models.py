from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.TextField()
    category = models.CharField(max_length=200)
    date =models.DateField()
    
    def str(self) -> str:
        return self.name



