from django.contrib import admin
from HomePage.models import Banner, Lancamento, Secao


class ImagensBanner(admin.ModelAdmin):
    list_display = ('id','titulo', 'ativo')
    list_display_links = ('id', 'titulo')
    list_editable = ('ativo',)

admin.site.register(Banner, ImagensBanner)

class Lancamentos(admin.ModelAdmin):
    list_display = ('id','titulo', 'posicao', 'ativo' )
    list_display_links = ('id', 'titulo')
    list_editable = ('posicao', 'ativo', )

admin.site.register(Lancamento, Lancamentos)

class Secoes(admin.ModelAdmin):
    list_display = ('id','titulo', 'ativo')
    list_display_links = ('id', 'titulo')
    list_editable = ('ativo',)

admin.site.register(Secao, Secoes)

