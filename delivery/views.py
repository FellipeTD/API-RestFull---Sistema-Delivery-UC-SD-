from django.shortcuts import render

# Create your views here.
from .models import user, estabelecimento,lista
from .serializers import userSerializer, estabelecimentoSerializer, listaSerializer
from rest_framework import viewsets, generics
from .serializers import userSerializer, estabelecimentoSerializer, listaSerializer, listaEstabelecimentoSerializer, listaUserSerializer

class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer

class estabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = estabelecimento.objects.all()
    serializer_class = estabelecimentoSerializer

class listaViewSet(viewsets.ModelViewSet):
    queryset = lista.objects.all()
    serializer_class = listaSerializer

class listaUser(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(user_id=self.kwargs['pk'])
        return queryset

    serializer_class = listaUserSerializer

class listaEstabelecimento(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(estabelecimento_id=self.kwargs['pk'])
        return queryset

    serializer_class = listaEstabelecimentoSerializer