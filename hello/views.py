from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def myView(request):               #pythonfunction receives http request
    return HttpResponse('Hello, World!') #returns response to http server