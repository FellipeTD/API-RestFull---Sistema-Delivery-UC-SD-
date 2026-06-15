from django.shortcuts import render

# Create your views here.
from .models import user, estabelecimento,lista, produto, pedido, endereco
from .serializers import userSerializer, estabelecimentoSerializer, listaSerializer, listaProdutoSerializer, \
    listaPedidoSerializer, listaEnderecoSerializer
from rest_framework import viewsets, generics
from .serializers import userSerializer, estabelecimentoSerializer, listaSerializer, listaEstabelecimentoSerializer, listaUserSerializer, produtoSerializer, pedidoSerializer, enderecoSerializer


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

class listaProduto(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(produto_id=self.kwargs['pk'])
        return queryset

    serializer_class = listaProdutoSerializer

class listaPedido(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(pedido_id=self.kwargs['pk'])
        return queryset

    serializer_class = listaPedidoSerializer

class listaEndereco(generics.ListAPIView):
    def get_queryset(self):
        queryset = lista.objects.filter(endereco_id=self.kwargs['pk'])
        return queryset

    serializer_class = listaEnderecoSerializer

class produtoViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = produto.objects.all()

    serializer_class = produtoSerializer

class pedidoViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = pedido.objects.all()

    serializer_class = pedidoSerializer


class enderecoViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        queryset = endereco.objects.all()

    serializer_class = enderecoSerializer