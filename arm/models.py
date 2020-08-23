from django.db import models

class Caregory(models.Model):
    name = models.CharField(max_length=255,verbose_name='Название категории')
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return  self.name