from django.shortcuts import render, redirect
from django.views.generic import View
from torneio.models import Grupo, Tecnico, Selecao, Jogador, Jogo, EventoJogo
from torneio.serializaers import GrupoSerializer, TecnicoSerializer, SelecaoSerializer, JogadorSerializer, JogoSerializer, EventoJogoSerializer
from rest_framework import viewsets


class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

class SelecaoViewSet(viewsets.ModelViewSet):
    queryset = Selecao.objects.all()
    serializer_class = SelecaoSerializer

class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer

class JogoViewSet(viewsets.ModelViewSet):
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer

class EventoJogoViewSet(viewsets.ModelViewSet):
    queryset = EventoJogo.objects.all()
    serializer_class = EventoJogoSerializer