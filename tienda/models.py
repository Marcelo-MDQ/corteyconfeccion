from django.db import models


# Create your models here.
class Producto(models.Model):
    # pongo el id aunque no es necesario
    # el problema que no me insertaba registros era que yo hacía los inserts forzando los ids
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100, default="", blank=True, null=True)
    largo = models.PositiveIntegerField(default=0)
    alto = models.PositiveIntegerField(default=0)
    profundidad = models.PositiveIntegerField(default=0)
    color = models.CharField(max_length=50, default="", blank=True, null=True)
    foto = models.ImageField(upload_to='libreria/static/img', verbose_name="Foto", null=True, blank=True)
    descripcion = models.TextField(verbose_name="Descripcion", blank=True, null=True)
 
    # para que se vea mejor en la parte de Admin
    def __str__(self):
        fila = self.nombre
        return fila

    # En el caso que tuviera una imagen guardada (versión anterior)
    #def delete(self, using=True, keep_parents=False):
    #    self.imagen.storage.delete(self.imagen.name)
    #    super().delete()
