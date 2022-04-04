from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length=40)
    numero=models.IntegerField()
    nacimiento=models.DateField()


    def __str__(self):
        return self.nombre

