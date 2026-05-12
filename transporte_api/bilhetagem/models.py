from django.db import models

class Municipio(models.Model):
    nome = models.CharField(max_length=120) # Nome do município
    uf = models.CharField(max_length=2) # Sigla do estado (ex.: RN, SP, RJ)
    endereco_sede = models.CharField(max_length=200, blank=True) # Endereço da prefeitura
    ativo = models.BooleanField(default=True)

class EmpresaTransporte(models.Model):
    razao_social = models.CharField(max_length=200)
    nome_fantasia = models.CharField(max_length=150, blank=True)
    cnpj = models.CharField(max_length=18, unique=True) # Formato 00.000.000/0000-00
    endereco = models.CharField(max_length=200, blank=True)
    municipio = models.ForeignKey(Municipio, on_delete=PROTECT, related_name='empresas')

class Usuario(models.Model):
    nome CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    cpf = models.CharField(max_length=14, unique=True) # Formato 000.000.000-00
    endereco = models.CharField(max_length=200, blank=True)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_cadastro = models.DataTimeField(auto_now_add=True)

class TipoTicket(models.Model):
    nome = models.CharField com choices # avulso, diario, semanal, mensal, anual
    descricao  = models.TextField(blank=True)
    valor = models.DecimalField(max_digits=8, decimal_places=2) # Preço do ticket
    duracao_dias = models.PositiveSmallIntegerField # 1 (avulso/diário), 7, 30, 365
    janela_integracao_minutos = models.PositiveSmallIntegerField(default=60) # Janela de integração tarifária em minutos
    ativo = models.BooleanField(default=True)

class Ticket(models.Model):
    status_choices =[
        ('ativo', 'ATIVO'),
        ('expirado', 'EXPIRADO'),
        ('cancelado', 'CANCELADO'),
        ('consumido', 'CONSUMIDO'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=PROTECT, related_name='tickets')
    tipo = models.ForeignKey(TipoTicket, on_delete=PROTECT, related_name='tickets')
    data_compra = models.DateTimeField(auto_now_add=True)
    valor_pago = models.DecimalField(max_digits=8, decimal_places=2)
    data_validade = models.DateTimeField() # Calculado a partir de data_compra + duracao_dias #########################################################
    status = models.CharField(max_length=10, choices=status_choices, default='ativo')

class Transporte(models.Model):
    tipo_choices = [
        ('parada', 'PARADA'),
        ('onibus', 'ONIBUS'),
        ('trem', 'TREM'),
    ]

    dentificacao = models.CharField(max_length=50, unique=True) #PARADA-001
    tipo = models.CharField(max_length=10, choices=tipo_choices)
    nome = models.CharField(max_length=150) # 'Parada Av. Roberto Freire' ou 'Linha 5 Verde'
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    empresa = models.ForeignKey(EmpresaTransporte, on_delete=PROTECT, related_name='transportes')
    ativo = models.BooleanField(default=True)

class Validador(models.Model):
    tipo_choices = [
        ('cartao', 'CARTÃO'),
        ('celular', 'CELULAR'),
    ]

    codigo = models.CharField(max_length=50, unique=True)
    tipo = models.CharField(max_length=10, choices=tipo_choices)
    transporte = models.ForeignKey(Transporte, on_delete=PROTECT, related_name='validadores', null=True, blank=True) # Nulo quando for celular do usuário
    data_instalacao = models.DateField()
    ativo = models.BooleanField(default=True)

class Validacao(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=PROTECT, related_name='validacoes')
    validador = models.ForeignKey(Validador, on_delete=PROTECT, related_name='validacoes')
    transporte = models.ForeignKey(Transporte, on_delete=PROTECT, related_name='validacoes')
    data_hora = models.DateTimeField(auto_now_add=True)
    dentro_janela_integracao = models.BooleanField(default=False) # True se ocorrer dentro da janela de 1h da validação anterior do mesmo usuário
    valor_debitado = models.DecimalField(max_digits=8, decimal_places=2, default=0) # Zero quando estiver dentro da janela de integração
