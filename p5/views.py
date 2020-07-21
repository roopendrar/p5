from django.http import HttpResponse
from django.shortcuts import render

def first(request):
    return HttpResponse("welcome to the home page")

def second(request):
    return render(request,"1.html")

def third(request):
    course=['fullstack','testing','datascience']
    return render(request,"directory/2.html",{'courses':course})

def fourth(request):
    return render(request,'directory/3.html',context={'number':9876543210})