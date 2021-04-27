from django.urls import path
from .views import Index, Curso

urlpatterns = [
    path('inicio/', Index.as_view(), name='inicio'),
    path('', Index.as_view(), name='inicio'),
    path('curso/', Curso.as_view(), name='curso'),
]
