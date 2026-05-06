from django.db import models
from django.db.models import PROTECT, SET_NULL, CASCADE

class Grupo(models.Model):
    nome = models.CharField(max_length=1)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"Grupo {self.nome} - {self.descricao}"


class Tecnico(models.Model):
    nome = models.CharField(max_length=150)
    nacionalidade = models.CharField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Selecao(models.Model):
    administracao_escolha = [
        ("UEFA", "UEFA"), ("CONMEBOL", "CONMEBOL"), 
        ("CONCACAF", "CONCACAF"), ("AFC", "AFC"), 
        ("CAF", "CAF"), ("OFC", "OFC"), 
    ]

    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3, unique=True)
    confederacao = models.CharField(max_length=10, choices=administracao_escolha)
    grupo = models.ForeignKey(Grupo, on_delete=PROTECT, related_name='selecoes')
    tecnico = models.OneToOneField(Tecnico, on_delete=SET_NULL, null=True, related_name='selecao')
    escudo_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nome} - {self.grupo.nome}"


class Jogador(models.Model):
    posicao_escolha = [
        ("goleiro", "Goleiro"), ("zagueiro", "Zagueiro"), ("lateral", "Lateral"), 
        ("volante", "Volante"), ("meia", "Meia"), ("atacante", "Atacante"), 
    ]

    nome = models.CharField(max_length=150)
    nome_guerra = models.CharField(max_length=50)
    selecao = models.ForeignKey(Selecao, on_delete=PROTECT, related_name='jogadores')
    posicao = models.CharField(max_length=10, choices=posicao_escolha)
    numero_camisa = models.PositiveSmallIntegerField()
    data_nascimento  = models.DateField()
    suspenso = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} - {self.selecao.nome}"

class Jogo(models.Model):
    fase_escolha = [
        ("grupos", "Grupos"), ("fase32", "Fase de 32"), ("oitavas", "Oitavas"), 
        ("quartas", "Quartas"), ("semifinal", "Semifinal"), ("final", "Final"), 
    ]
    status_escolha = [
        ("agendado", "Agendado"), ("em_andamento", "Em Andamento"), 
        ("encerrado", "Encerrado"), ("cancelado", "Cancelado"), 
    ]

    selecao_mandante = models.ForeignKey(Selecao, related_name='jogos_mandante', on_delete=PROTECT)
    selecao_visitante = models.ForeignKey(Selecao, related_name='jogos_visitante', on_delete=PROTECT)
    fase = models.CharField(max_length=10, choices=fase_escolha)
    grupo = models.ForeignKey(Grupo, on_delete=PROTECT, null=True, blank=True) 
    data_hora = models.DateTimeField()
    estadio = models.CharField(max_length=150, blank=True)
    cidade = models.CharField(max_length=100, blank=True)
    gols_mandante = models.PositiveSmallIntegerField(default=0)
    gols_visitante = models.PositiveSmallIntegerField(default=0)
    status = models.CharField(max_length=15, choices=status_escolha, default="agendado")

    def __str__(self):
        return f"{self.selecao_mandante} x {self.selecao_visitante} - {self.fase}"


class EventoJogo(models.Model):
    tipo_escolha = [
        ("gol", "Gol"), ("cartao_amarelo", "Cartão Amarelo"),
        ("cartao_vermelho", "Cartão Vermelho"), ("gol_contra", "Gol Contra"), 
    ]

    jogo = models.ForeignKey(Jogo, on_delete=CASCADE, related_name='eventos')
    jogador = models.ForeignKey(Jogador, on_delete=PROTECT, related_name='eventos')
    tipo = models.CharField(max_length=20, choices=tipo_escolha)
    minuto = models.PositiveSmallIntegerField()
    acrescimo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tipo} - {self.minuto}' - {self.jogador.nome}"