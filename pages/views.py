from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = "home.html"

class Curso(TemplateView):
    template_name = "curso.html"
