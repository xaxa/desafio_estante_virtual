from django.test import TestCase
from jogos_olimpicos.models import Atleta,Competicao,Resultado
from rest_framework.exceptions import APIException
from django.test import Client

class CompeticaoModelTest(TestCase):
    def setUp(self):
        Competicao.objects.create(nome="Dardo semifinal",quantidade_chances=1,finalizada=True,criterio_vencedor="maior")
        Competicao.objects.create(nome="100m classificatoria",quantidade_chances=1,finalizada=False,criterio_vencedor="maior")
        
    def teste_finalizado(self):
        with self.assertRaisesMessage(APIException, "Competição finalizada"):
            competicao_dardo = Competicao.objects.get(nome="Dardo semifinal")
            competicao_dardo.nome = "Dardo final"
            competicao_dardo.save()

        competicao_corrida = Competicao.objects.get(nome="100m classificatoria")
        competicao_corrida.nome = "100m final"
        competicao_corrida.save()
        self.assertEqual(competicao_corrida.nome, "100m final")

class ResultadoModelTest(TestCase):
    def setUp(self):
        Atleta.objects.create(nome="Carlos")
        Competicao.objects.create(nome="Dardo semifinal",quantidade_chances=1,finalizada=True,criterio_vencedor="maior")
        Competicao.objects.create(nome="100m classificatoria",quantidade_chances=1,finalizada=False,criterio_vencedor="maior")


    def teste_salvar_dados_competicao_finalizada(self):
        atleta = Atleta.objects.get(nome="Carlos")
        competicao_dardo = Competicao.objects.get(nome="Dardo semifinal")
        with self.assertRaisesMessage(APIException, "Competição finalizada"):
            Resultado.objects.create(competicao=competicao_dardo, atleta=atleta, valor="30", unidade="m")


    def teste_maximo_tentativas_atleta(self):
        atleta = Atleta.objects.get(nome="Carlos")
        competicao_corrida = Competicao.objects.get(nome="100m classificatoria")

        Resultado.objects.create(competicao=competicao_corrida, atleta=atleta, valor="8", unidade="s")
        with self.assertRaisesMessage(APIException, "Atleta já teve quantidade de partipação máxima."):
            Resultado.objects.create(competicao=competicao_corrida, atleta=atleta, valor="7", unidade="s")

class AtletaViewTest(TestCase):
    def setUp(self):
        self.client = Client()
 
    def teste_criacao_nome_vazio(self):
        response = self.client.post('/atleta/',{"nome":""}, format="json")
        self.assertEqual(response.status_code, 400) #se falhar, retorna erro 400

class CompeticaoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
 
    def teste_criterio_vencedor_valor_indevido(self):
        response = self.client.post('/competicao/',{"nome":"Dardo","quantidade_chances":"1","finalizada":"True","criterio_vencedor":"media"}, format="json")
        self.assertEqual(response.status_code, 400) #se falhar, retorna erro 400

class ResultadoViewTest(TestCase):
    def setUp(self):
        Atleta.objects.create(nome="Carlos")
        Competicao.objects.create(nome="100m classificatoria",quantidade_chances=1,finalizada=False,criterio_vencedor="maior")
        self.client = Client()
 
    def teste_unidade_valor_indevido(self):
        response = self.client.post('/resultado/',{"competicao":1, "atleta":1, "valor":8, "unidade":"h"}, format="json")
        self.assertEqual(response.status_code, 400) #se falhar, retorna erro 400