from django.urls import path
from .views import FruitView, InfoView

urlpatterns = [
    path('', FruitView.as_view(), name='fruit_app'),
    path('info', InfoView.as_view(), name='fruit_app_info')
]