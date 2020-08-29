from django.contrib import admin

from catrige.models import Color, Firm, PrinterModel, CatrigeModel, Status, Catrige, PrinterStatus, Printer

class ColoraAdmin(admin.ModelAdmin):
    list_display = ['name']

class FirmAdmin(admin.ModelAdmin):
    list_display = ['name']

class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ['name','firm']
    search_fields = ['name']

class CatigeModelAdmin(admin.ModelAdmin):
    list_display = ['name','color', 'printer_model']

class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']

class CatrigeAdmin(admin.ModelAdmin):
    list_display = ['catrige_models','serialNamber','status','date']
    search_fields = ['serialNamber']

class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ['name']

class PrinterAdmin(admin.ModelAdmin):
    list_display = ['printer_model','serial_number','ip','printer_status','discription']
    search_fields = ['serial_number','ip']

admin.site.register(Color, ColoraAdmin)
admin.site.register(Firm, FirmAdmin)
admin.site.register(PrinterModel, PrinterModelAdmin)
admin.site.register(CatrigeModel, CatigeModelAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Catrige,CatrigeAdmin)
admin.site.register(PrinterStatus,PrinterStatusAdmin)
admin.site.register(Printer, PrinterAdmin)




