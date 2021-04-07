from django.shortcuts import render
from .models import Destination
import time 

a=0
b=1
c=2
d=3
# Create your views here.
def index(request):
    dest = Destination.objects.all()
    return render(request,'index.html',{'dest':dest})