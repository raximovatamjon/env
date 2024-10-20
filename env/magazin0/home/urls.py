from django.urls import path
from .views import index,single

urlpatterns=[
                      path('',index,name='index.html'),
                      path('single',single,name='single.html'),
                      path('product/<int:id>/',single,name='product')
                      
                      
]
