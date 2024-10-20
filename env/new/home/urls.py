from django.urls import path
from .views import about,blog,contact,index,service

urlpatterns=[
                      path('about',about,name='about'),
                      path('blog',blog,name='blog'),
                      path('contact',contact,name='contact'),
                      path('',index,name='index'),
                      path('service',service,name='service')
]