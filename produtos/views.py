from produtos.models import Produto, Colecao, VariacaoProduto
from rest_framework import viewsets
from produtos.serializer import ProdutoSerializer, ColecaoSerializer, VariacoesSerializer

class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer


class ColecoesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer

class VaricoesViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = VariacaoProduto.objects.all()
    serializer_class = VariacoesSerializer

