from dataclasses import field, fields
from rest_framework import serializers
from clientes import models


class GruposSerializers(serializers.ModelSerializer):    
    class Meta:
        model = models.Grupos
        fields = '__all__'


class ClientesSerializers(serializers.ModelSerializer):    

    GruposSerializers(many=True, read_only=False)
    class Meta:
        model = models.Usuarios
        #fields = ['id_user', 'nome_completo','idade', 'sexo','email',
        #'telefone','pais','estado','cidade','bairro','logradouro','status','grupo','usuarios',]
        fields = '__all__'