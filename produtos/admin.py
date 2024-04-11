from django.contrib import admin
from produtos.models import Produto, Colecao, VariacaoProduto

class Colecoes(admin.ModelAdmin):
    list_display = ('id','titulo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20

admin.site.register(Colecao, Colecoes)
# Register your models here.
class Produtos(admin.ModelAdmin):
    list_display = ('id','titulo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20

admin.site.register(Produto, Produtos)

class VariacoesProdutos(admin.ModelAdmin):
    list_display = ('id','titulo')
    list_display_links = ('id', 'titulo')
    search_fields = ('titulo',)
    list_per_page = 20

admin.site.register(VariacaoProduto, VariacoesProdutos)

