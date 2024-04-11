
from django.contrib import admin
from django.urls import path,include
from produtos.views import ProdutosViewSet, ColecoesViewSet, VaricoesViewSet
from clientes.views import ClientesViewSet
from HomePage.views import BannerViewSet, LancamentoViewSet, SecaoViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register('variacoesProdutos', VaricoesViewSet, basename='VariacoesProdutos')
router.register('produtos', ProdutosViewSet, basename='Produtos')
router.register('colecoes', ColecoesViewSet, basename='Colecoes')
router.register('clientes', ClientesViewSet, basename='Clientes')
router.register('homePagebanner', BannerViewSet, basename='BannerImagens')
router.register('homePageLancamentos', LancamentoViewSet, basename='Lancamentos')
router.register('homePageSecoes', SecaoViewSet, basename='Secoes')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)