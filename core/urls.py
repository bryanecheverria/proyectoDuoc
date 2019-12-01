from django.urls import path
from .views import home,post,agregarPost,crearLogin,eliminarPost,Modificar,modificarPost






urlpatterns = [
    path('',home, name="inicio"),
    path('post/',post, name='post'),
    path('agregar-post/',agregarPost, name = 'agregarPost'),
    path('registrar-form/', crearLogin , name= 'registrar-form'),
    path('modificar/',Modificar, name='modificar'),
    path('eliminar-post/<id>/',eliminarPost, name='eliminarPost'),
    path('modificar-post/<id>/',modificarPost, name='modificarPost'),
  ]
