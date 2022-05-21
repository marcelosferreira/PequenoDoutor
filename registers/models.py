from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry, ADDITION
from datetime import datetime


# Create your models here.
#criar os modelos do site e fazer os migrates pro banco
#criar telas de cadastro
class Professor(models.Model):
	nomeProfessor = models.CharField(max_length=255)
	emailProfessor = models.CharField(max_length=255)
	senhaProfessor = models.CharField(max_length=255)
	avatarProfessor = models.FileField(upload_to="media/%Y/%m/%d/")
	
	def __str__(self):
		return self.nomeProfessor


class Aula(models.Model):
	nomeAbreviadoAula = models.CharField(max_length=255)
	nomeCompletoAula = models.CharField(max_length=255)
	textoAula = models.CharField(max_length=255)
	textoAdicionalAula = models.CharField(max_length=255)
	linkAula = models.CharField(max_length=255, default=None, blank=True, null=True)

	def __str__(self):
		return self.nomeAbreviadoAula


class Curso(models.Model):
	nomeCurso = models.CharField(max_length=255)
	variosAtributosCurso = models.CharField(max_length=255)
	quantidadeAulasCurso = models.CharField(max_length=255)
	categoriaCurso = models.CharField(max_length=255)
	professorCurso = models.ForeignKey(Professor, on_delete=models.CASCADE)
	imagemCurso = models.FileField(upload_to="media/curso/%Y/%m/%d/",default=None, blank=True, null=True)
	aulaCurso = models.ManyToManyField(Aula)

	def __str__(self):
		return self.nomeCurso


class Turma(models.Model):
	idTurma = models.CharField(max_length=255)
	nomeTurma = models.CharField(max_length=255)
	cursoTurma = models.ForeignKey(Curso, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.nomeTurma


class Aluno(models.Model):
	nomeAluno = models.CharField(max_length=255)
	emailAluno = models.CharField(max_length=255)
	avatarAluno = models.CharField(max_length=255)
	userAluno = models.ForeignKey(User, on_delete=models.PROTECT)
	turmaAluno = models.ForeignKey(Turma, on_delete=models.PROTECT, blank=True, null=True)
	
	def __str__(self):
		return self.nomeAluno

class Chat(models.Model):
	pergunta = models.CharField(max_length=1000000)
	respostaA = models.CharField(max_length=1000000)
	respostaB = models.CharField(max_length=1000000)
	respostaC = models.CharField(max_length=1000000)
	respostaD = models.CharField(max_length=1000000)
	
	def __str__(self):
		return self.pergunta

class Room(models.Model):
    name = models.CharField(max_length=1000)
    turmaRoom = models.ForeignKey(Turma, on_delete=models.CASCADE, blank=True, null=True)

class Message(models.Model):
    value = models.CharField(max_length=1000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)

class Quiz(models.Model):
	pergunta = models.CharField(max_length=1000000)
	respostaA = models.CharField(max_length=1000000)
	respostaB = models.CharField(max_length=1000000)
	respostaC = models.CharField(max_length=1000000)
	respostaD = models.CharField(max_length=1000000)

	def __str__(self):
		return self.pergunta
