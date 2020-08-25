import datetime
from django.contrib import admin
from person.models import Person, Position, Department

@admin.register(Department)
class  Department(admin.ModelAdmin):
    list_display = ['dep_name']



@admin.register(Position)
class Position(admin.ModelAdmin):
    list_display = ['pos_name']



@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display = ('first_name','last_name','father_name','phone')






