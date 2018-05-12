from rest_framework import serializers
from jogos_olimpicos.models import Atleta,Competicao,Resultado




class AtletaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Atleta
        fields = ('id','nome')

class ResultadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Resultado
        fields = ('competicao','atleta','valor','unidade')


class CompeticaoSerializer(serializers.ModelSerializer):        

    class Meta:
        model = Competicao
        fields = ('id','nome','quantidade_chances','finalizada','criterio_vencedor')