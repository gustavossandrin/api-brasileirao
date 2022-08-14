from rest_framework import serializers

from brasileirao.times.models import Times


class TimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Times
        fields = ('id', 'nome')

