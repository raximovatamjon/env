from django.shortcuts import render
from .models import Product

# Create your views here.

def blog(req):
                             return render(req,'blog.html')

def contact(req):
                             return render(req,'contact.html')
                             
def index(req):
                             data=Product.objects.all()
                             context={
                                                          'data':data
                             }
                             return render(req,'index.html')


def service(req):
                             return render(req,'service.html')
def shop(req):
                             return render(req,'shop.html')