from django.db import models

class Zone(models.Model):
    name = models.CharField(max_length=40, verbose_name='Название зоны')

    class Meta:
        verbose_name = 'Зона'
        verbose_name_plural = 'Зоны'

    def __str__(self):
        return self.name

class Titul(models.Model):
    name = models.CharField(max_length=30, verbose_name='Титул')
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, verbose_name='Зона')

    class Meta:
        verbose_name = 'Титул'
        verbose_name_plural = 'Титулы'


    def __str__(self):
        return '{}'.format(self.name)



class Room(models.Model):
    titul = models.ForeignKey(Titul,on_delete=models.CASCADE,verbose_name='Титул')
    name = models.CharField(max_length=100,verbose_name='Кабинет')



    class Meta:
        verbose_name = 'Кабинет'
        verbose_name_plural = 'Кабинеты'

    def __str__(self):
        return self.name

