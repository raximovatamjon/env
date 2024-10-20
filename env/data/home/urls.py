from django.urls import path
from .views import index,single

urlpatterns=[
                      path('',index,name='index'),
                      path("product/<int:id>/",single,name='product'),
                      
]
