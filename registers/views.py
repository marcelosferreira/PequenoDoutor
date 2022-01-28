from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Professor, Aluno, Turma, Aula, Chat, Room, Message
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse

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

class SobreView(TemplateView):
    template_name = "about.html"


#View do Almanaque
class Almanaque(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'almanaque.html'

    def get_queryset(self):
        self.object_list = Aluno.objects.filter(userAluno=self.request.user)
        return self.object_list

#View do Pequeno Doutor
class PequenoDoutor(TemplateView):
    template_name = "pequenoDoutorB.html"

# VIEWS DO CHAT
class ChatView(LoginRequiredMixin, ListView):
    model = Chat
    template_name = 'teste.html'

    def get_queryset(self):
        self.object_list = Chat.objects.filter(userAluno=self.request.user)
        return self.object_list



def home(request):
    return render(request, 'homeB.html')

def room(request, room):
    #username = request.GET.get('username')
    if request.user.is_authenticated:
        username = Aluno.objects.get(userAluno = request.user)
        #print(username.turmaAluno)
        room_details = Room.objects.get(turmaRoom = username.turmaAluno)
    return render(request, 'room.html', {
        'username': username,
        'room': room_details.name,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})
