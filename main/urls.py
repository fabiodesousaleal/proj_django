from django.urls import path, include
from .views import mod_quest

urlpatterns = [
    path('', mod_quest)
]