from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home (request):
    	return render(request,"home.html")

def help(request):
        return render(request,"help.html")

def about (request):
        return render(request,"about.html")


