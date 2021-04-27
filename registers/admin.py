from django.contrib import admin

# Register your models here.
from registers.models import Professor
from registers.models import Aluno
from registers.models import Curso
from registers.models import Turma
from registers.models import Aula

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Aula)
