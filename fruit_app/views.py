from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

import json

from .fruits_db import fruits

# Create your views here.

class FruitView(View):
    def get(self, request):
        return render(request, 'fruit_app/fruitlist.html', {'fruits': fruits})