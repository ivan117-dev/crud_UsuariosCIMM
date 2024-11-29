from django.db import models
import os
# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nac = models.DateField()
    usuario= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    foto= models.ImageField(upload_to='usuarios_fotos', blank=True, null= True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    
    #Eliminar imagen
    def delete(self, *args, **kwargs):
        if self.foto:
            if os.path.isfile(self.foto.path):
                os.remove(self.foto.path)
        super().delete(*args, **kwargs)