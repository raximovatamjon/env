from django.shortcuts import render

# Create your views here.

def home (req):
    return render(req,'index.html')


def contact (req):
    return render(req,'contact.html')


def trainer (req):
    return render(req,'trainer.html')


def why(req):
    return render (req,'why.html')




    











