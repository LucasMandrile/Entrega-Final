from cgitb import html
from django.contrib import admin
from .models import *
#from django.utils.html import format_html
# Register your models here.

#Personalizar panel de administracion
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'status','creado_el','autor',)
    list_filter = ("status",)
    search_fields = ['titulo', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}

    #def foto(self,obj):
        #return format_html('<img src={} width="100" heiggt="100" />', obj.imagenPost.url)
admin.site.register(Post,PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'active')
    list_filter = ('active', 'creado_el')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
