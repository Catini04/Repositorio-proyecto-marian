from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from app.forms import RegistroUsuarioForm , UserEditForm
from django.contrib.auth import login, authenticate
from .models import post




def inicio(request):
    return render (request,'paginas/inicio.html')
def registro(request):
    if request.method == 'POST':
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request,'paginas/inicio.html',{"mensaje":f"El usuario {username} fue creado corretamente"})
        else:
            return render(request,'paginas/registro.html',{"mensaje": "No se pudo crear el usuario, intentelo nuevamente"})

    else:
        form = RegistroUsuarioForm()
        return render(request,'paginas/registro.html', {"form": form})


    return render (request,'paginas/registro.html')
def ingreso(request):
        if request.method == 'POST':
            form=AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                info=form.cleaned_data
                usuario=info['username']
                password=info['password']
                verificacion_de_existencia_de_usuario=authenticate(username=usuario, password=password)
                if verificacion_de_existencia_de_usuario is not None:
                    login( request , verificacion_de_existencia_de_usuario)
                    return render(request,'paginas/inicio.html',{"mensaje":f"Bienvendio {usuario}, logueado correctamente"})
                else:
                    return render(request,'paginas/login.html',{"form":form,"mensaje":"Usuario o contraseña incorrectos"})
            else:
                return render(request,'paginas/login.html',{"form":form,"mensaje":"Usuario o contraseña incorrectos"})

        else:
            form = AuthenticationForm()
            return render(request,'paginas/login.html',{"form": form})

def sobremi(request):
    return render (request,'paginas/sobremi.html')
def editarperfil(request):
    usuario=request.user

    if request.method=='POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.password1=info["password1"]
            usuario.password2=info["password2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render (request,'paginas/editarperfil.html',{"mensaje" : f"Editado correctamente"})
        else:
            return render (request,'paginas/editarperfil.html',{"form": form})
    else:
        form = UserEditForm(instance = usuario)
        return render (request,'paginas/editarperfil.html',{"form": form})
def posteo(request):
    a = post.objects.all()
    
    return render(request,'paginas/posteo.html',{"mostrar": a})




