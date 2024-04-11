from rest_framework import serializers
from HomePage.models import Banner, Lancamento, Secao

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class LancamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lancamento
        fields = '__all__'


class SecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Secao
        fields = '__all__'



