from django.urls import path
from arm.views import ListCategoryView

urlpatterns = [
   path('', ListCategoryView.as_view(),name='category'),
]