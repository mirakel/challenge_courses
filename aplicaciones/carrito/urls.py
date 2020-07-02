from django.urls import path, re_path
from .views import *


urlpatterns = [
    re_path(r'^agregar_carrito_compra/(?P<slug>[^/]+)/$', agregar_curso_carrito, name='p_agregar_compra'),
    re_path(r'^ver_carrito/(?P<usuario>[^/]+)$', ver_carrito, name='p_ver_carrito'),
]
