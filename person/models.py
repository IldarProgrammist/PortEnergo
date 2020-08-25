from django.db import models
from time import timezone


class Department(models.Model):
    dep_name = models.CharField(max_length=40,verbose_name='Отдел')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.dep_name




class Position(models.Model):
    pos_name = models.CharField(max_length=100, verbose_name='Должность')
    slug = models.SlugField(unique=True)


    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.pos_name




class Person(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Фамилия')
    last_name = models.CharField(max_length=50, verbose_name='Имя')
    father_name = models.CharField(max_length=55, verbose_name='Отчество')
    phone = models.CharField(max_length=15, verbose_name='Номер телефона')
    mobile_phone = models.CharField(max_length=15, verbose_name='Мобильный номер телефона', blank=True)
    mail  = models.EmailField(blank=True, verbose_name='Электронная почта')
    photo = models.ImageField(blank=True, verbose_name='Фото', upload_to='media/')
    dep = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='Отдел')
    pos = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Должность')



    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return '{}{}'.format(self.first_name,self.last_name)


