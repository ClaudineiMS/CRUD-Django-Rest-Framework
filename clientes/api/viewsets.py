from rest_framework import viewsets
from clientes.api import serializers
from clientes import models


class ClientesViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClientesSerializers
    queryset = models.Usuarios.objects.all()

class GruposViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GruposSerializers
    queryset = models.Grupos.objects.all()
