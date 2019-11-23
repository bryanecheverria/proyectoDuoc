from django.urls import path
from .views import home,post,agregarPost,crearLogin






urlpatterns = [
    path('',home, name="inicio"),
    path('post/',post, name='post'),
    path('agregar-post/',agregarPost, name = 'agregarPost'),
    path('registrar-form/', crearLogin , name= 'registrar-form'),
    

  ]
