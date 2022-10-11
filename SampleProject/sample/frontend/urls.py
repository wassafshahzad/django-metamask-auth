from django.urls import path, include
from .views import indexView

urlpatterns = [
    path('', indexView),
]