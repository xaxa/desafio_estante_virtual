from rest_framework import serializers
from jogos_olimpicos.models import Atleta,Competicao,Resultado
from django.db.models import Min,Max,Q
from functools import reduce
import operator

class AtletaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atleta
        fields = ('id','nome')

class ResultadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resultado
        fields = ('competicao','atleta','valor','unidade')

class ResultadoSimplesSerializer(serializers.ModelSerializer):
    atleta = serializers.ReadOnlyField(source='atleta.nome')
    valor = serializers.DecimalField(max_digits=6, decimal_places=3)
    unidade = serializers.CharField(max_length=1)

    class Meta:
        model = Resultado
        fields = ('atleta','valor','unidade')

class CompeticaoSerializer(serializers.ModelSerializer):

    resultados = serializers.SerializerMethodField()