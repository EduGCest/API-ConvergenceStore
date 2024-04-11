from django.shortcuts import render
from HomePage.serializer import BannerSerializer, LancamentoSerializer, SecaoSerializer
from rest_framework import viewsets
from HomePage.models import Banner, Lancamento, Secao

class BannerViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class LancamentoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Lancamento.objects.all()
    serializer_class = LancamentoSerializer

class SecaoViewSet(viewsets.ModelViewSet):
    """Exibindo todos os produtos"""
    queryset = Secao.objects.all()
    serializer_class = SecaoSerializer
