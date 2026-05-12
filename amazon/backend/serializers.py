from rest_framework import serializers
from .models import Cliente, Endereco, FormaPagamento, Vendedor, Item, Pedido, ItemPedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' # Inclui todos os campos do modelo
        # Para expor apenas alguns campos, use uma lista:
        # fields = ['id', 'nome', 'email']
        # Para excluir campos, use:
        # exclude = ['data_cadastro']

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__' # Inclui todos os campos do modelo
        # Para expor apenas alguns campos, use uma lista:
        # fields = ['id', 'nome', 'email']
        # Para excluir campos, use:
        # exclude = ['data_cadastro']

class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = '__all__' # Inclui todos os campos do modelo
        # Para expor apenas alguns campos, use uma lista:
        # fields = ['id', 'nome', 'email']
        # Para excluir campos, use:
        # exclude = ['data_cadastro']

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__' # Inclui todos os campos do modelo
        # Para expor apenas alguns campos, use uma lista:
        # fields = ['id', 'nome', 'email']
        # Para excluir campos, use:
        # exclude = ['data_cadastro']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' # Inclui todos os campos do modelo
        # Para expor apenas alguns campos, use uma lista:
        # fields = ['id', 'nome', 'email']
        # Para excluir campos, use:
        # exclude = ['data_cadastro']

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__' # Inclui todos os campos do modelo
        # Para expor apenas alguns campos, use uma lista:
        # fields = ['id', 'nome', 'email']
        # Para excluir campos, use:
        # exclude = ['data_cadastro']

class ItemPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPedido
        fields = '__all__' # Inclui todos os campos do modelo
        # Para expor apenas alguns campos, use uma lista:
        # fields = ['id', 'nome', 'email']
        # Para excluir campos, use:
        # exclude = ['data_cadastro']