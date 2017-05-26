from django.contrib import admin
from .models import Noticia, Categoria

class CategoriaAdmin(admin.ModelAdmin):
	list_display = ('nome', 'slug')
	prepopulated_fields = {'slug': ('nome',)}

admin.site.register(Categoria, CategoriaAdmin)


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'autor', 'publish', 'status', 'categoria')
    list_filter = ('status', 'publish', 'autor')
    search_fields = ('titutlo', 'noticia_texto')
    prepopulated_fields = {'slug': ('titulo',)}
    raw_id_fields = ('autor',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(Noticia, NoticiaAdmin)