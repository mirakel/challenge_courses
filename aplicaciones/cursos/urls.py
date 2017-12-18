from django.conf.urls import url
from .views import *

# from django.views.static.
urlpatterns = [
    url(r'^$', Curso.as_view(), name='p_inicio'),
]
