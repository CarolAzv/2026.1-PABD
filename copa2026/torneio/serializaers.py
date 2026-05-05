from rest_framework import serializers
from .models import Grupo, Tecnico, Selecao, Jogador, Jogo, EventoJogo

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = '__all__'


class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = '__all__'


class SelecaoSerializer(serializers.ModelSerializer):
    tecnico_nome = serializers.CharField(source='tecnico.nome', read_only=True)

    class Meta:
        model = Selecao
        fields = '__all__'


class JogadorSerializer(serializers.ModelSerializer):
    posicao_display = serializers.CharField(source='get_posicao_display', read_only=True)
    class Meta:
        model = Jogador
        fields = '__all__'


class EventoJogoSerializer(serializers.ModelSerializer):
    jogador_nome = serializers.CharField(source='jogador.nome_guerra', read_only=True)
    tipo_display = serializers.CharField(source='get_tipo_display', read_only=True)
    class Meta:
        model = EventoJogo
        fields = '__all__'


class JogoSerializer(serializers.ModelSerializer):
    mandante_nome = serializers.CharField(source='selecao_mandante.nome', read_only=True)
    visitante_nome = serializers.CharField(source='selecao_visitante.nome', read_only=True)
    fase_display = serializers.CharField(source='get_fase_display', read_only=True)
    eventos = EventoJogoSerializer(many=True)
    resultado = serializers.SerializerMethodField()

    def get_resultado(self, obj):
        if obj.gols_mandante > obj.gols_visitante:
            return 'Mandante venceu'
        elif obj.gols_mandante < obj.gols_visitante:
            return 'Visitante venceu'
        else:
            return 'Empate'

    class Meta:
        model = Jogo
        fields = '__all__'