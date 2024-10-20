from django.urls import path
from .views import crud,post

urlpatterns = [
    path('',crud,name='home'),
    path('post',post,name='post')
]
