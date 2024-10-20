from django.shortcuts import render
from .models import maxsulot

def index(req):
                             data=maxsulot.objects.all()
                             
                             context={
                                                          'data':data
                             } 
                                                      
                             return render(req,'index.html',context)

def single(req,id):
                             data=maxsulot.objects.get(id=id)
                             
                             context={
                                                          'data':data
                             }
                             
                             return render(req,'single.html',context)