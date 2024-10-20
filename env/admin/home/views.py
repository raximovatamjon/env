from django.shortcuts import render
from .models import Mahsulot

def home(req):
    data = Mahsulot.objects.all()
    context = {
        'data':data
    }
    return render(req,'index.html',context)


def single(req,id):
    data = Mahsulot.objects.get(id=id)
    context = {
        "data":data
    }
    return render(req,'single.html',context)