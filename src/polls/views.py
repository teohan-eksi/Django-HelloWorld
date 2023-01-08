from django.shortcuts import render
from django.http import HttpResponse
from mysite import settings

# Create your views here.

def index(request):
    response_object = "response"

    return HttpResponse(response_object)