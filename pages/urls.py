from django.urls import path
from .views import Index, Curso, PequenoDoutor, PequenoDoutorB, Chat

urlpatterns = [
    path('inicio/', Index.as_view(), name='inicio'),
    #path('', Index.as_view(), name='inicio'),
    path('curso/', Curso.as_view(), name='curso'),
    #path('almanaque', Almanaque.as_view(), name='almanaque'),
    #path('pequenoDoutor', PequenoDoutor.as_view(), name='pequenoDoutor'),
    path('pequenoDoutorB', PequenoDoutorB.as_view(), name='pequenoDoutor'),
]
