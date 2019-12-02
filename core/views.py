from django.shortcuts import render, redirect
from .models import  UpdatePost
from .form  import UserCustomForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth  import login, authenticate
from django.contrib import messages
# Create your views here.



def home(request):
    post = UpdatePost.objects.all()

    variable= {'post':post }
   
    return render(request,'core/inicio.html',variable)
    







@login_required
def agregarPost(request):
 
        registro = UpdatePost.objects.all()
        variable ={'registro':registro }

       
        if request.POST:
            post = UpdatePost()
            post.titulo =  request.POST.get('txt_titulo')
            post.valor = request.POST.get('txt_valor')
            post.descripcion= request.POST.get('txt_descripcion')
            post.imagen0 = request.FILES.get('txt_imagen0')
            post.imagen1 = request.FILES.get('txt_imagen1')
            post.imagen2 = request.FILES.get('txt_imagen2')
            
            try:
                post.save()
                variable['mensaje']='guardado correctamente'
            except:
                  variable['mensaje']='no se ha podido  guardar'
    
        return render(request,'core/agregarpost.html', variable)




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

def post(request,id):
    post =UpdatePost.objects.get(id=id)

    return render(request,'core/post.html',{'post':post})

def eliminarPost(request,id):

    post = UpdatePost.objects.get(id=id)

    
    try:
        post.delete()
        mensaje="eliminado correctamente"
        messages.success(request, mensaje)
    except:
        mensaje="no se pudo eliminar correctamente"
        messages.error(request,mensaje)

        
    return  redirect('core/listar_post.html')


def Modificar(request):
        
        post = UpdatePost.objects.all()

        variable= {'post':post }
   
        return render(request,'core/listar_post.html',variable)



def modificarPost(request,id):
    post = UpdatePost.objects.get(id=id)
    variable ={ 'post':post}
    if request.POST:
            post.titulo =  request.POST.get('txt_titulo')
            post.valor = request.POST.get('txt_valor')
            post.descripcion= request.POST.get('txt_descripcion')
            post.imagen = request.FILES.get('txt_imagen')
            post.save()
            try:
                post.save()
                variable['mensaje']='se modifico correctamente'
            except:
                  variable['mensaje']='error al modificar'
        
    
    

    return render(request,'core/modificar_post.html',variable)



    
     


    
      


        


        










