from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AlunoCreate, AlunoList, Aluno, CursoDetail, CursoView, ChatView, Almanaque, Quiz, PequenoDoutor, SobreView
from . import views


urlpatterns = [
        path('login/', auth_views.LoginView.as_view(
            template_name='home.html'
        ), name='login'),
        path('', auth_views.LoginView.as_view(
            template_name='home.html'
        ), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('registers/alunoNovo/', AlunoCreate.as_view(), name='alunoCreate'),
        path('aluno/', AlunoList.as_view(), name='alunoList'),
        path('sobre/', SobreView.as_view(), name='sobre'),
        path('chat/', ChatView.as_view(), name='chat'),
        path('curso-detalhe/<int:pk>', CursoView.as_view(), name='cursoDetail'),
        #URL DO MANUAL DST
        path('almanaque', Almanaque.as_view(), name='almanaque'),
        #URL DO PEQUENO DOC
        path('pequenoDoutor', PequenoDoutor.as_view(), name='pequenoDoutor'),
        #URL DO QUIZ
        path('quiz', Quiz.as_view(), name='quiz'),
        #URLS DO CHAT
        path('testee', views.home, name='home'),
        path('sala/', views.room, name='sala'),
        path('checkview', views.checkview, name='checkview'),
        path('send', views.send, name='send'),
        path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
        
]