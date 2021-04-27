from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Professor, Aluno, Turma, Aula
from django.urls import reverse_lazy

# Create your views here.

class AlunoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Aluno
    fields = ['nomeAluno', 'emailAluno', 'avatarAluno'] #userAluno não está pq o cadastro é automat
    template_name = 'form.html'
    success_url = reverse_lazy('listar-alunos')

    #funcao para editar o formulario de cadastro
    def form_valid(self, form):

        #pegando o userAluno do formulário e atribuindo o valor do user logado 
        form.instance.userAluno = self.request.user
        url = super().form_valid(form)
        return url

class AlunoList(LoginRequiredMixin, ListView):
    model = Aluno
    template_name = 'curso.html'

    def get_queryset(self):
        #self.object_list = Aluno.objects.all() O comum, mesmo que nada
        self.object_list = Aluno.objects.filter(userAluno=self.request.user)
        return self.object_list

class CursoDetail(LoginRequiredMixin, DetailView):
    model = Aluno
    template_name = 'cursoDetalhes.html'

    def get_object(self):
        return Aluno.objects.get(turmasAluno=self.kwargs['pk'])


class CursoView(LoginRequiredMixin, ListView):
    template_name = 'cursoDetalhes.html'
    context_object_name = 'cursolista'

    def get_queryset(self):
        self.object_list = Aluno.objects.filter(userAluno=self.request.user)
        return self.object_list

    def get_context_data(self, **kwargs):
        context = super(CursoView, self).get_context_data(**kwargs)
        context['cursolista'] = Turma.objects.filter(pk=self.kwargs['pk'])
        #context['aulalista'] = Aula.objects.filter(cursoAula=self.kwargs['pk'])
        return context
