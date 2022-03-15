from django.urls import path
from blog.views import *

urlpatterns = [
    path('inicio/', inicio, name='Inicio'),
    path('quienSoy', quien_soy, name='QuienSoy'),
    path('post_list', PostList.as_view(), name='home'),
    #la expresion <slug:slug> captura los valores de la URL y devolver la página de detalles de la publicación equivalente
    #path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    #reenplazo la vista de detalles por la funcion post_detail
    path('<slug:slug>/',post_detail, name='post_detail'),
    path('post/create', PostCreate.as_view(), name='crearPost'),
    path('post/update/<slug:slug>/', PostUpdate.as_view(), name='modificarPost'),
    path('post/delete/<slug:slug>/', PostDelete.as_view(), name='eliminarPost'),
    #path('comentarios',verComentarios, name='comentarios'),
    

    ]
