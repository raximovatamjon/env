from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def chiqar(req):                             
                             return render(req,'index.html')
                             return render(req,'style.css')