from django.urls import path
from .views import blog,contact,index,service,shop

urlpatterns=[
                      path('blog',blog,name='blog.html'),
                      path('contact',contact,name='contact.html'),
                      path('',index,name='index.html'),
                      path('service',service,name='service.html'),
                      path('shop',shop,name='shop.html'),
                      path("product/<int:id>/",blog,name='product'),
                      
]
