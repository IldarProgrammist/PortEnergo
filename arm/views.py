from django.shortcuts import render
from django.views.generic import ListView

from arm.models import Caregory


class ListCategoryView(ListView):
    model = Caregory
    queryset = Caregory.objects.all()
    template_name ='arm/ListCategory.html'
    context_object_name = 'Category'


