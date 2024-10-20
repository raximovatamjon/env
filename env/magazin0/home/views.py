from django.shortcuts import render
from .models import Product

# Create your views here.

def index(req):
                             data=Product.objects.all()
                             context={
                                                          'data':data
                             }
                             return render(req,'index.html',context)

def single(req):
                             return render(req,'single.html')

