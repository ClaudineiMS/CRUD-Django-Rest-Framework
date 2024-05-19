from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.usuarios_create, name='usuarios_create'),
    path('grupos/', views.grupos_create, name='grupos_create'),
    path('lista_de_grupos', views.grupos_consulta, name='grupos_consulta'),
    path('lista_de_usuarios', views.usuarios_consulta, name='usuarios_consulta'),
    path('<id>/deletar/', views.grupo_deletar, name='grupo_deletar'),
    path('<id>/deletar_usuario/', views.usuario_deletar, name='usuario_deletar'),
    path('<id>/update', views.update_view, name = 'update_view'),
    path('<id>/update_usuario', views.update_view_user, name = 'update_view_user'),
    path('lista_de_grupos_edit', views.grupos_consulta_edit, name='grupos_consulta_edit'),
    path('lista_de_usuarios_edit', views.usuarios_consulta_edit, name='usuarios_consulta_edit'),
    path('lista_de_grupos_excluir', views.grupos_consulta_excluir, name='grupos_consulta_excluir'),
    path('lista_de_usuarios_excluir', views.usuarios_consulta_excluir, name='usuarios_consulta_excluir'),
    

]