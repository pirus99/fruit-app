from django.urls import path
from .views import FruitView

urlpatterns = [
    path('', FruitView.as_view(), name='fruit_app')
]