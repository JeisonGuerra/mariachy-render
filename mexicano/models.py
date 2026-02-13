from django.db import models   
import os
from django.conf import settings


class Noticia(models.Model):
    """Una noticia"""
    encabezado=models.CharField(max_length=200)
    noticia=models.TextField()
    clave=models.CharField(max_length=50)
    fecha=models.DateTimeField(auto_now_add=True)
    imagen=models.ImageField(upload_to='imagenes/')
    alt=models.CharField()
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        if len(self.noticia)>50:
            return f"{self.noticia[:100]}..."
        else: return f"{self.noticia[:100]}"
        
    
class MarquetingVideo(models.Model):
    """Un elemento de marqueting"""
    alt=models.CharField(max_length=200)
    video=models.FileField(upload_to='marketing/videos/')
    fecha=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.alt
    
    
class MarquetingFoto(models.Model):
    """Un elemento de marqueting"""
    alt=models.CharField(max_length=200)
    imagen=models.FileField(upload_to='marketing/imagenes/')
    fecha=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.alt
    
    
class Cancion(models.Model):
    """Una cancion para la pleylist"""
    titulo=models.CharField(max_length=200)
    cancion=models.FileField(upload_to='audios/')
    fecha=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.titulo
    
    
class Video(models.Model):
    """Un video para la coleccion"""
    fecha=models.DateTimeField(auto_now_add=True)
    titulo=models.CharField(max_length=200)
    video=models.FileField(upload_to='videos/')
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.titulo
    
    
class Foto(models.Model):
    """Una foto de la galeria"""
    imagen_small=models.ImageField(upload_to='imagenes/')
    imagen=models.ImageField(upload_to='imagenes/')
    alt=models.CharField()
    fecha=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.alt


class Estrellas(models.Model):
    cantidad=models.IntegerField()
    calificacion=models.FloatField()
    calificacion_aprox=models.IntegerField()


class Resena(models.Model):
    nombre=models.CharField(max_length=100)
    comentario=models.TextField()
    calificacion=models.IntegerField()
    fecha=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.comentario

    
class Contratacion(models.Model):
    """Descripcion del contrato"""
    descripcion=models.TextField()
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.descripcion
    
    
class Contacto(models.Model):
    """Un contacto"""
    tipo=models.CharField(max_length=200)
    contacto=models.CharField(max_length=200)
    fecha=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return f"{self.tipo}: {self.contacto}"
    
    
class Eslogan(models.Model):
    """Un eslogan"""
    eslogan=models.CharField(max_length=200)
    fecha=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devuelve una representación del modelo como cadena."""
        return self.eslogan