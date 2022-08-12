
from rest_framework import viewsets, filters

from brasileirao.jogadores.models import Jogador
from brasileirao.jogadores.serializers import JogadorSerializer


class JogadorViewSet(viewsets.ModelViewSet):
    queryset = Jogador.objects.all()
    serializer_class = JogadorSerializer
    filter_backends = [filters.SearchFilter]
    filterset_fields = ['nome', 'time', 'idade', 'posicao']
