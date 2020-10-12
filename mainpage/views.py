from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests
from requests.compat import quote_plus
from . import models


# Create your views here.
def index(request):
    return render(request, 'mainpage/index.html')


def home(request):
    return render(request, 'mainpage/base.html')


def contact(request):
    return render(request, 'mainpage/contact.html')
