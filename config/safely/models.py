from django.db import models

# Create your models here.
class person(models.Model):
    number= models.CharField(max_length=18, verbose_name='Número de Celular')
    name = models.CharField(max_length=150, verbose_name='Nombre')
    correo = models.CharField(max_length=150, verbose_name='Correo Electrónico')
    
    def ___str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)