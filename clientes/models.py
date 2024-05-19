from pickletools import uint4
from django.db import models
from uuid import uuid4
#from django.utils.deconstruct import deconstructible



#@deconstructible
class Usuarios(models.Model):
    
    SEXO_CHOICES = (
        ("Feminino", "Feminino"),
        ("Masculino", "Masculino"),
        ("Nenhuma das opções", "Nenhuma das opções")
    )

    STATUS_CHOICES = (
        ("Ativo", "Ativo"),
        ("Inativo", "Inativo"),
    )

    id_user = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    nome_completo = models.CharField(max_length=255)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=30, choices=SEXO_CHOICES, blank=False, null=False)
    email = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, blank=False, null=False)
    grupo = models.ForeignKey("Grupos", on_delete=models.CASCADE)

   
    

class Grupos(models.Model):
    
    STATUS_CHOICES = (
        ("Ativo", "Ativo"),
        ("Inativo", "Inativo"),
    )
    
    id_grupo = models.UUIDField(primary_key=True, default=uuid4, editable=False, unique=True)
    titulo = models.CharField(max_length=200)
    descricao = models.CharField(max_length=500)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, blank=False, null=False)
    criado = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo



