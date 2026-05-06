from django.contrib import admin
from .models import Grupo, Tecnico, Selecao, Jogador, Jogo, EventoJogo

admin.site.register(Grupo)
admin.site.register(Tecnico)
admin.site.register(Selecao)
admin.site.register(Jogador)
admin.site.register(Jogo)
admin.site.register(EventoJogo)