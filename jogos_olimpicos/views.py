from jogos_olimpicos.models import Atleta,Competicao,Resultado
from jogos_olimpicos.serializers import AtletaSerializer,CompeticaoSerializer,ResultadoSerializer
from rest_framework import viewsets


class AtletaViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer

class CompeticaoViewSet(viewsets.ModelViewSet):
    queryset = Competicao.objects.all()
    serializer_class = CompeticaoSerializer



class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer



