from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


from .forms import  UserEditionForm, UserRegisterForm, Perfil
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
    
    if request.method == 'POST':
        miForm = UserEditionForm(request.POST)
        
        if miForm.is_valid():
            info= miForm.cleaned_data
            
            usuario.email = info['email']
            usuario.first_name= info['first_name']
            usuario.last_name= info['last_name']
            new_password = info['password1']
            usuario.set_password(new_password)
             
            
            usuario.save()

            return redirect('home')
    else:
        miForm = UserEditionForm(initial={'email': usuario.email,'first_name':usuario.first_name ,'last_name': usuario.last_name,'password':usuario.password})
        
        return render(request, 'AppLogin/editarPerfil.html',{'miForm':miForm, 'usuario':usuario})

def verPerfil(request):
    usuario = request.user
    perfil = Perfil.objects.filter(user=usuario)
    
    username= usuario.username
    
    email= usuario.email
    avatar= usuario.perfil.imagenPerfil
    print(username)
    

    return render(request, "AppLogin/perfil.html", {'username':username,'email':email, 'usuario':usuario})


