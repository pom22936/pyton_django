from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World</h1></br><b>Welcome to my libraly</b>")

# Create your views here.
