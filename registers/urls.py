from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AlunoCreate, AlunoList, Aluno, CursoDetail, CursoView


urlpatterns = [
        path('login/', auth_views.LoginView.as_view(
            template_name='home.html'
        ), name='login'),
        path('logout/', auth_views.LogoutView.as_view(), name='logout'),
        path('registers/alunoNovo/', AlunoCreate.as_view(), name='alunoCreate'),
        path('aluno/', AlunoList.as_view(), name='alunoList'),
        path('curso-detalhe/<int:pk>', CursoView.as_view(), name='cursoDetail'),

]