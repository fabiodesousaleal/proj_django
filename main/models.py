from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Questao(models.Model):
    enunciado = models.TextField()
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.enunciado

class Alternativa(models.Model):
    descricao = models.TextField()
    alternativa_verdadeira = models.BooleanField(default=False)
    questao = models.ManyToManyField("Questao")

    def __str__(self):
        return self.descricao