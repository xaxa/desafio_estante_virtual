from django.db import models


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

    def __str__(self):
        return self.nome

    

class Resultado(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    competicao = models.ForeignKey(Competicao, on_delete=models.CASCADE,null=False, blank=False)
    atleta = models.ForeignKey(Atleta, on_delete=models.CASCADE,null=False, blank=False)
    valor = models.DecimalField(max_digits=6, decimal_places=3, blank=False)
    unidade = models.CharField(choices=UNIDADES,max_length=1,blank=False)

    class Meta:
        ordering = ('valor',)



