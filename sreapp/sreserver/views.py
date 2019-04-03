from django.shortcuts import render,HttpResponse,Http404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from . import models

# Create your views here.
def get_data(request):
    return HttpResponse('hello')
