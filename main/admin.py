from django.contrib import admin

# Register your models here.
from .models import Questao, Disciplina, Assunto, Comentario

admin.site.register(Questao)
admin.site.register(Disciplina)
admin.site.register(Assunto)
admin.site.register(Comentario)

