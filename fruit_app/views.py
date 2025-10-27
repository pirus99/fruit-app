from django.shortcuts import render
from django.http import JsonResponse, Http404
from django.views import View

import json

from .fruits_db import fruits

# Create your views here.

class FruitView(View):
    def get(self, request):
        try:
            return render(request, 'fruit_app/fruitlist.html', {'fruits': fruits})
        except:
            raise Http404()
    
class InfoView(View):
    def get(self, request):
        try:
            return render(request, 'fruit_app/info.html')
        except:
            raise Http404()