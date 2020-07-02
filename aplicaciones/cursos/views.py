from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
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


class CourseDetailView(DetailView):
    template_name = 'cursos/detalle_curso.html'

    def get_queryset(self):
        self.name = get_object_or_404(mis_cursos, slug=self.kwargs['slug'])
        return mis_cursos.objects.filter(nombre=self.name)

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView,
                        self).get_context_data(**kwargs)
        context['curso'] = mis_cursos.objects.get(nombre=self.name)
        return context
