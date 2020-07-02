from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Curso as mis_cursos
# Create your views here.


class Curso(TemplateView):
    template_name = 'cursos/cursos.html'

    def get_context_data(self, **kwargs):
        context = super(Curso,
                        self).get_context_data(**kwargs)
        context['cursos'] = mis_cursos.objects.all()
        return context


class Index_principal(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index_principal,
                        self).get_context_data(**kwargs)
        context['cursos'] = mis_cursos.objects.filter(estado=True)
        return context
