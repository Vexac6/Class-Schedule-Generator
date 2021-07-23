from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),
    url(r'^orario_personale/$', views.orario_docente, name='orario_d'),
    url(r'^(?P<facolta_id>[0-9]+)/$', views.orario_facolta, name='orario_f'),
]
