from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^$', Curso.as_view(), name='p_inicio'),
    re_path(r'^detalle_curso/(?P<slug>[^/]+)/$', CourseDetailView.as_view(), name='detalle_curso'),
]
