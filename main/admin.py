from django.contrib import admin

# Register your models here.
from .models import Alternativa, Questao, Disciplina

admin.site.register(Alternativa)
admin.site.register(Questao)
admin.site.register(Disciplina)
