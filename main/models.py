from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.nome

class Assunto(models.Model):
    nome = models.CharField(max_length=200)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)


    def __str__(self):
        return self.nome

class Questao(models.Model):
    enunciado = models.TextField(null=False)
    assunto = models.ForeignKey(Assunto, on_delete=models.CASCADE)
    alternativa = models.ManyToManyField("Alternativa")

    def __str__(self):
        return self.enunciado

class Alternativa(models.Model):
    descricao = models.TextField(null=False)
    alternativa_verdadeira = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao