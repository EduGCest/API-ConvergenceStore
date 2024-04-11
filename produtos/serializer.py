from rest_framework import serializers
from produtos.models import Produto, Colecao, VariacaoProduto

class ColecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colecao
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class VariacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariacaoProduto
        fields = '__all__'