from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from blog.models import Post, Comment


from .forms import  *
from django.contrib.auth.models import User
import django

# Create your views here.
# Vista Login
def login_request(request):
    
    if request.method == 'POST':
        #Validación del formulario
        form = AuthenticationForm(request, data=request.POST)


        if form.is_valid():
            usuario = form.data.get('username')
            passwd = form.data.get('password')

            #Django valida usuario y contraseña.
            #Si el usuario es OK, crea cache y redirecciona.
            #Si el usuario está mal, redirecciona a la vista Login.
            user = authenticate(username=usuario, password=passwd)

            if user:
                login(request, user)

                return redirect('home')
            else:
                return redirect('Login')
                

        else:
            return redirect('Login')
    
    form = AuthenticationForm()

    return render(request, 'AppLogin/login.html', {'form': form})

#vista registro
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.data['username']
            try:
                user_new = User.objects.get(username=username)
            except django.contrib.auth.models.User.DoesNotExist:
                user_new = None

            if not user_new:
                form.save()

            return redirect('Login')

    else:
        form = UserRegisterForm()

    return render(request, 'AppLogin/register.html', {'form': form})

def editarUsuario(request):
    usuario = request.user
    if not usuario.is_authenticated:
        return redirect('home')
    perfil = request.user.perfil

    if request.method == 'POST':
        userForm = UserRegisterForm(request.POST,instance = usuario)
        imageForm=UserImageForm(request.POST,request.FILES, instance=perfil)

        if userForm.is_valid() and imageForm.is_valid():
            infoUser= userForm.cleaned_data
            infoImage= imageForm.cleaned_data
            
            usuario.email = infoUser['email']
            usuario.first_name= infoUser['first_name']
            usuario.last_name= infoUser['last_name']
            new_password = infoUser['password1']
            usuario.set_password(new_password)
             
            
            perfil.imagenPerfil= infoImage['imagenPerfil']

            usuario.save()

            perfil.save()    

            return redirect('home')
    else:
        
        userForm = UserRegisterForm(initial={'email': usuario.email,'first_name':usuario.first_name ,'last_name': usuario.last_name})
        imageForm = UserImageForm()
    return render(request, 'AppLogin/editarPerfil.html',{'userForm':userForm,'imageForm':imageForm , 'usuario':usuario})

def verPerfil(request):
    usuario = request.user
    perfil = Perfil.objects.filter(user=usuario)
    comentarios= Comment.objects.filter(name=usuario)

    username= usuario.username
    #userBio= usuario.perfil.biografia
    email= usuario.email
    avatar= usuario.perfil.imagenPerfil
    print(username)
    print(comentarios)

    return render(request, "AppLogin/perfil.html", {'username':username,'email':email, 'usuario':usuario,'comentario':comentarios})

"""Para ver los comentarios"""                                           

def verComentarios(request):
    comentario= Comment.objects.filter(name=request.user)
   
    return render(request,"Applogin/comentarios.html", {'comentario':comentario})
