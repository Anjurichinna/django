from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(requests):
	return render(requests,'home.html');

def index(requests):
	return render(requests,'index.html');

def add(request):
	name=0
	num1 = request.GET["n1"]
	num2 = request.GET["n2"]
	return render(request,'results.html',{'num1':num1,'num2':num2});
	