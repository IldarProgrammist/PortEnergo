from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from catrige.models import Catrige, Printer


def CatrigeListView(request):
    catrige = Catrige.objects.all()
    return render(request, 'catrige/catriges.html', {'catrige':catrige})

def PrinterListView(request):
    printer = Printer.objects.all()
    return render(request, 'catrige/printer.html', {'printer': printer})


