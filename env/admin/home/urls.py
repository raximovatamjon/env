from django.urls import path
from .views import home,single

urlpatterns = [
    path('',home,name='home'),
    path("product/<int:id>/",single, name="product")
]
