from django.core import paginator
from django.shortcuts import render
from person.models import Person
from  django.views.generic import ListView
from  django.db.models import  Q
from  django.core.paginator import  Paginator

# class personListView(ListView):
#
#     model = Person
#     context_object_name = 'person'
#     paginate_by = 2
#     template_name = 'person/person.html'
#     queryset = Person.objects.order_by('first_name')


def ListPersonView(request):
    person = Person.objects.all()
    searchQwery = request.GET.get('search','')

    if searchQwery:
        person = Person.objects.filter(Q(first_name__contains=searchQwery)|Q(last_name__contains=searchQwery))
    else:
        person = Person.objects.all().order_by('first_name')


    paginator = Paginator(person,2)
    page_number = request.GET.get('page',1)
    page = paginator.get_page(page_number)

    is_paginate = page.has_other_pages()

    if page.has_previous():
        prev_url ="?page={}".format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url ="?page={}".format(page.next_page_number())
    else:
        next_url = ''

    context ={
        'person': page,
        'is_paginate': is_paginate,
        'next_url': next_url,
        'prev_url': prev_url

        }


    return render(request,'person/person.html', context=context)
