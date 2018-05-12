from jogos_olimpicos.models import Atleta,Competicao,Resultado
from jogos_olimpicos.serializers import AtletaSerializer,CompeticaoSerializer,ResultadoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import action
from rest_framework import viewsets

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'atleta': reverse('atleta-list', request=request, format=format),
        'competicao': reverse('competicao-list', request=request, format=format),
        'resultado': reverse('resultado-list', request=request, format=format)
    })


class AtletaViewSet(viewsets.ModelViewSet):
    queryset = Atleta.objects.all()
    serializer_class = AtletaSerializer

class CompeticaoViewSet(viewsets.ModelViewSet):
    queryset = Competicao.objects.all()
    serializer_class = CompeticaoSerializer

    @action(detail=True)
    def finalizarCompeticao(self, request, *args, **kwargs):
        competicao = self.get_object()
        competicao.finalizada = True
        competicao.save()
        return Response(CompeticaoSerializer(competicao).data)

class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer



