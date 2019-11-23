from django.shortcuts import render, redirect
from .models import  UpdatePost
from .form  import UserCustomForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import login, authenticate
# Create your views here.



def home(request):
    post = UpdatePost.objects.all()

    variable= {'post':post }
   
    return render(request,'core/inicio.html',variable)
    







@login_required
def agregarPost(request):
   
        if request.POST:
            post = UpdatePost()
            post.titulo =  request.POST.get('txt_titulo')
            post.valor = request.POST.get('txt_valor')
            post.descripcion= request.POST.get('txt_descripcion')
            post.imagen = request.FILES.get('txt_imagen')
            post.save()

     


        return render(request,'core/agregarpost.html')









def crearLogin(request):
    data={ 'form':UserCustomForm()}

    if request.method == 'POST':
        formulario =  UserCustomForm(request.POST)
        if formulario.is_valid():
             formulario.save()
             username = formulario.cleaned_data['username']
             password = formulario.cleaned_data['password1']
             user= authenticate(username=username, password=password)
             login(request,user)
             return redirect(to='inicio')
            

    return render(request, 'registration/registrar.html',data)

def post(request):
    return render(request,'core/post.html')









