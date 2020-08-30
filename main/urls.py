
from django.urls import path
from main.views import mainView


urlpatterns = [
    path('',mainView, name= 'main')
]