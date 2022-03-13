from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('login/', login_request, name='Login'),
    path('logout/', LogoutView.as_view(template_name='AppLogin/logout.html'), name='Logout'),
    path('register/', register, name='Register'),
    path('editarPerfil/', editarUsuario, name="editarPerfil"),
]

