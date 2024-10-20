from django.urls import path
from .views import i,uy,manzil,contact,about

urlpatterns=[
                      path('',i),
                      path('uy',uy),
                      path('manzil',manzil),
                      path('about',about),
                      path('contact',contact),
                      
]