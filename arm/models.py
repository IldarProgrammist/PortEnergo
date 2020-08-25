from django.db import models

class Caregory(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return  self.name


class Firm(models.Model):
    name = models.CharField(max_length=70, verbose_name='Название')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Фирма'
        verbose_name_plural = 'Фирмы'

    def __str__(self):
        return  self.name


class Model(models.Model):
    name = models.CharField(max_length=70, verbose_name='Модель')
    slug = models.CharField(max_length=20, unique=True)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, verbose_name='Фирма')

    def __str__(self):
        return  self.name


class Product(models.Model):

    class Meta:
        abstract = True

    category = models.ForeignKey(Caregory, on_delete=models.CASCADE, verbose_name='Категория')
    model = models.ForeignKey(Model,on_delete=models.CASCADE, verbose_name='Модель')
    serial_namber = models.CharField(max_length=255, verbose_name='Серийный номер')
    slug = models.SlugField(unique=True)
    image = models.ImageField(blank=True)
    discription = models.TextField(verbose_name='Описание', blank=True )

    def __str__(self):
        return  "{}".format(self.serial_namber, self.category)



class OperationSystem(models.Model):
    name = models.CharField(max_length=20, verbose_name='Операционная система')

    class Meta:
        verbose_name_plural = 'Операционные системы'
        verbose_name = 'Операционая система'

    def __str__(self):
        return self.name



class PC(Product):
    hd = models.CharField(max_length=255, verbose_name='Размер жесткого диска')
    ram = models.CharField(max_length=255, verbose_name='Размер оперативной памяти')
    os = models.ForeignKey(OperationSystem, on_delete= models.CASCADE,  verbose_name='Операционная система')

    def __str__(self):
        return self.os



class NoteBook(Product):
    title = models.CharField(max_length=255, verbose_name='Название')
    hd = models.CharField(max_length=255, verbose_name='Размер жесткого диска')
    ram = models.CharField(max_length=255, verbose_name='Размер оперативной памяти')
    os = models.ForeignKey(OperationSystem, on_delete= models.CASCADE,  verbose_name='Операционная система')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'






