from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from brasileirao.times.models import Times
from brasileirao.times.serializers import TimesSerializer


class TimesViewSet(viewsets.ModelViewSet):
    queryset = Times.objects.all()
    serializer_class = TimesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome']
