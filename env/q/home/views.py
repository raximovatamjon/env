from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def i(req):
                             return render(req,'i.html')
def uy(req):
                             return render(req,'uy.html')

def manzil(req):
                             return render(req,'manzil.html')
def about(req):
                             return render(req,'about.html')
def contact(req):
                             return render(req,'contact.html')


