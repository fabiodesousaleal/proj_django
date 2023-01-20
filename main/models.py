from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=200, null=False)
    def __str__(self):
        return self.nome

class Assunto(models.Model):
    nome = models.CharField(max_length=200)
    disciplina_id = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Questao(models.Model):
    enunciado = models.TextField(null=False)
    alternativa1 = models.TextField(null=False)
    alternativa2 = models.TextField(null=True)
    alternativa3 = models.TextField(null=True)
    alternativa4 = models.TextField(null=True)
    alternativa5 = models.TextField(null=True)
    assunto_id = models.ForeignKey(Assunto, on_delete=models.CASCADE)
    resposta = models.IntegerField(null=False)
    nivel_dificuldade = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    data_questao_inserida = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.enunciado

class Comentario(models.Model):
    descricao = models.TextField(null=True)
    questao_id = models.ForeignKey(Questao, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.descricao

