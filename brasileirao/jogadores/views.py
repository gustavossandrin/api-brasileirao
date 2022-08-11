from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from brasileirao.jogadores.models import Jogador
from brasileirao.jogadores.serializers import JogadorSerializer


class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'time', 'idade', 'posicao']
