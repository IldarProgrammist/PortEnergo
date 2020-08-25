from django.contrib import admin
from django.forms import ModelChoiceField

from arm.models import Caregory, NoteBook, OperationSystem


#
# @admin.register(Caregory)
# class Caregory(admin.ModelAdmin):
#     list_display = ['name']



class NoteBookAdmin(admin.ModelAdmin):

   def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return  ModelChoiceField(Caregory.objects.filter(slug='noteboks'))

        return super().formfield_for_foreignkey(db_field, request, **kwargs)



class OsAdmin(admin.ModelAdmin):
    pass



admin.site.register(Caregory)
admin.site.register(NoteBook, NoteBookAdmin)
admin.site.register(OperationSystem, OsAdmin )

