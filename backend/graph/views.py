from django.shortcuts import render
from django.http import HttpResponse
import graphyte

def index(request):
    graphyte.send('graph_index.count', 5)
    return HttpResponse("Hello, world.")
