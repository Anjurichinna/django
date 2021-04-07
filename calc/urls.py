from django.urls import path 
from . import views 


urlpatterns = [
path('',views.home,name="home"),
path('new/',views.index,name="index"),
path('add',views.add,name="add")
]
