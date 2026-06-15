from rest_framework import serializers
from .models import user,estabelecimento,lista,produto,pedido,endereco

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id','nome','email','cpf','data_nascimento','celular']

class estabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = estabelecimento
        fields = '__all__'

class listaSerializer(serializers.ModelSerializer):
    class Meta:
        model = lista
        exclude = []

class listaUserSerializer(serializers.ModelSerializer):
    estabelecimento = serializers.ReadOnlyField(source='estabelecimento.descricao')

    class Meta:
        model = lista
        fields = ['estabelecimento']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class listaEstabelecimentoSerializer(serializers.ModelSerializer):
    user_nome = serializers.ReadOnlyField(source='user.nome')

    class Meta:
        model = lista
        fields = ['user_nome']

class produtoSerializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = '__all__'

class pedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = pedido
        fields = '__all__'

class enderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = endereco
        fields = '__all__'

class listaProdutoSerializer(serializers.ModelSerializer):
    user_nome = serializers.ReadOnlyField(source='user.nome')

    class Meta:
        model = lista
        fields = ['user_nome']

class listaPedidoSerializer(serializers.ModelSerializer):
    user_nome = serializers.ReadOnlyField(source='user.nome')

    class Meta:
        model = lista
        fields = ['user_nome']

class listaEnderecoSerializer(serializers.ModelSerializer):
    user_nome = serializers.ReadOnlyField(source='user.nome')

    class Meta:
        model = lista
        fields = ['endereco']