from django.contrib import admin
from person.models import Person


@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = ('first_name','last_name','father_name','phone')
