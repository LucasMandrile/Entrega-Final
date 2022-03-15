from django.shortcuts import render

# Importaciones desde Django
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
# Create your views here.

def inicio(request):
    return render(request, 'blog/inicio.html')

"""vista para listar post"""
class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-creado_el')
    template_name = 'blog/post_list.html'

""""vista para ver detalles del post"""
class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

""""vista para crear post"""
class PostCreate(CreateView):
    model = Post
    success_url = "/blog/post_list"
    fields = ['titulo','autor','status','contenido','slug']

"""vista para modificar post"""
class PostUpdate(UpdateView):
    model = Post
    success_url = "/blog/post_list"
    fields = ['titulo','status','contenido']

"""vista para eliminar un post"""
class PostDelete(DeleteView):
    model = Post
    success_url = "/blog/post_list"



"""vista basada en funciones, para modificar la vista detalles y que nos figuren los comentarios en la misma"""
def post_detail(request, slug):
    template_name = 'blog/post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

#"""Para ver los comentarios"""                                           

#def verComentarios(request):
#    comentario= Comment.objects.filter(name=request.user)
   
#    return render(request,"blog/comentarios.html", {'comentario':comentario})


