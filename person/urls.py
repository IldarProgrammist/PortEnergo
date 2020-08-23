
from django.urls import path

#get_search_person
#from person.views import personListView,
from person.views import ListPersonView

urlpatterns = [
   # path('', personListView.as_view(),name='person'),
    path('',ListPersonView, name= 'person')
]