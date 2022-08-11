from rest_framework import serializers

from brasileirao.jogadores.models import Jogador


class JogadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogador
        fields = ('id', 'nome', 'time', 'idade', 'posicao')
