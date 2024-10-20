from django.shortcuts import render

# Create your views here.

def about (req):
                             return render(req,'about.html')
def contact (req):
                             return render(req,'contact.html')
def index (req):
                             return render(req,'index.html')
def service (req):
                             return render(req,'service.html')