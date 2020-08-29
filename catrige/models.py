from django.db import models

class Color(models.Model):
    name = models.CharField(max_length=30,verbose_name='Цвет', unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name

class Firm(models.Model):
    name = models.CharField(max_length=50, verbose_name='Фирма', unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Фирма принтера'
        verbose_name_plural = 'Фирмы принтеров'

    def __str__(self):
        return self.name


class PrinterModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Модель принтера', unique=True)
    firm = models.ForeignKey(Firm, on_delete = models.CASCADE, verbose_name='Фирма')
    photo = models.ImageField(blank=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Модель принтера'
        verbose_name_plural = 'Модели принтеров'

    def __str__(self):
        return self.name


class CatrigeModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название модели', unique=True)
    color = models.ForeignKey(Color,on_delete=models.CASCADE, verbose_name='Цвет')
    printer_model = models.ForeignKey(PrinterModel, on_delete=models.CASCADE, verbose_name='Модель принтера')
    slug = models.SlugField(unique=True)
    class Meta:
        verbose_name = 'Модель  картриджа'
        verbose_name_plural = 'Модели картриджей'

    def __str__(self):
        return self.name



class Status(models.Model):
    name = models.CharField(max_length=40, verbose_name='Статус', unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Статус картриджа'
        verbose_name_plural = 'Статусы картриджей'

    def __str__(self):
        return self.name

class Catrige(models.Model):
    catrige_models = models.ForeignKey(CatrigeModel, on_delete=models.CASCADE, verbose_name='Модель картриджа')
    serialNamber = models.CharField(max_length=30, verbose_name='Серийный номер')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Картридж'
        verbose_name_plural = 'Картриджи'

    def __str__(self):
        return self.serialNamber

class PrinterStatus(models.Model):
    name = models.CharField(max_length=30, verbose_name='Стаутс принтера')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Статус принтера'
        verbose_name_plural = 'Статусы принтеров'

    def __str__(self):
        return self.name



class Printer(models.Model):
    printer_model = models.ForeignKey(PrinterModel, on_delete= models.CASCADE, verbose_name='Модель принтера')
    serial_number = models.CharField(max_length=100, verbose_name='серийные номре')
    ip = models.CharField(max_length=30, verbose_name='ip-адрес')
    printer_status = models.ForeignKey(PrinterStatus, on_delete=models.CASCADE, verbose_name='Статус принтера')
    discription = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Принтер'
        verbose_name_plural = 'Принтеры'

    def __str__(self):
        return self.serial_number




