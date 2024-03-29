from django.db import models

# Create your models here.



 
class  UpdatePost(models.Model):
    titulo = models.CharField(max_length=50)
    valor = models.FloatField()
    descripcion = models.CharField(max_length=200)
    imagen0 = models.ImageField(upload_to="post-image",null=True)
    imagen1 = models.ImageField(upload_to="post-image",null=True)
    imagen2 = models.ImageField(upload_to="post-image",null=True)
   
   
       

    

class Consultar(models.Model):
    nombre = models.CharField(max_length=20)
    celular = models.IntegerField()
    correo= models.EmailField()
    descripcion= models.CharField(max_length=100)
    post = models.ForeignKey(UpdatePost, on_delete=models.CASCADE)
    
    def __str__(self):
      return self.nombre


    
   
    