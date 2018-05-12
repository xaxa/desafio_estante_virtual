from django.db import models
from django.db.models.signals import pre_save
from rest_framework.exceptions import APIException
UNIDADES = (
		('s','Segundos'),
		('m','Metros'),
	)
CRITERIO_VENCEDOR = (
        ('maior','Maior valor'),
        ('menor','Menor valor'),
    )
class Atleta(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=150, blank=False)

    def __str__(self):
        return self.nome


class Competicao(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    nome = models.CharField(max_length=150, blank=False) 
    quantidade_chances = models.SmallIntegerField( blank=False)
    finalizada = models.BooleanField(default=False)
    criterio_vencedor = models.CharField(choices=CRITERIO_VENCEDOR,max_length=5,blank=False)

    def __str__(self):
        return self.nome

    @staticmethod
    def validar_finalizada(sender, instance, **kwargs):
        if instance.id:
            competicao = Competicao.objects.get(pk=instance.pk)
            if competicao.finalizada:
                raise APIException("Competição finalizada")

class Resultado(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE,null=False, blank=False)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE,null=False, blank=False)
    valor = models.DecimalField(max_digits=6, decimal_places=3, blank=False)
    unidade = models.CharField(choices=UNIDADES,max_length=1,blank=False)

    class Meta:
        ordering = ('valor',)

    @staticmethod
    def validar_quantidade_participacao(sender, instance, **kwargs):
        competicao = Competicao.objects.get(pk=instance.competicao_id)
        atleta = Atleta.objects.get(pk=instance.atleta_id)
        total_resultados_atleta = Resultado.objects.filter(competicao=competicao,atleta=atleta).count()
        if total_resultados_atleta >= competicao.quantidade_chances:
            raise APIException("Atleta já teve quantidade de partipação máxima.")

    @staticmethod
    def validar_competicao_finalizada(sender, instance, **kwargs):
        competicao = Competicao.objects.get(pk=instance.competicao_id)
        if competicao.finalizada:
            raise APIException("Competição finalizada")


pre_save.connect(Competicao.validar_finalizada,Competicao)
pre_save.connect(Resultado.validar_competicao_finalizada,Resultado)
pre_save.connect(Resultado.validar_quantidade_participacao,Resultado)


