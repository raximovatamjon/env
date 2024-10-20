from django.shortcuts import render
from .models import Todo

# Create your views here.

def crud(req):
     
     return render(req,'index.html')
     
def post(req):
     title=req.GET['title']
     dec=req.GET['dect']
     data=Todo(title=title,discription=dec)
     data.save()
     context={
          'title':title,
          'dec':dec
     }
     return render(req,'post.html',context)
