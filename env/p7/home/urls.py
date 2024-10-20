from django.urls import path
from .views import home,contact,trainer,why

urlpatterns = [
    path('',home,name= "home"),
    path ('contact',contact, name="contact"),
    path('trainer',trainer, name= "trainer"),
    path ('why',why, name="why")

]