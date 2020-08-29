from django.urls import path
from catrige.views import CatrigeListView, PrinterListView

urlpatterns = [
   path('',CatrigeListView, name='catrige'),
   path('printer/', PrinterListView, name='printer'),
]