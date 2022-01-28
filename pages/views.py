from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = "home.html"

class Curso(TemplateView):
    template_name = "curso.html"

#class Almanaque(TemplateView):
#    template_name = "almanaque.html"

class PequenoDoutor(TemplateView):
    template_name = "pequenoDoutor.html"

class PequenoDoutorB(TemplateView):
    template_name = "pequenoDoutorB.html"

class Chat(TemplateView):
    template_name = "teste.html"
