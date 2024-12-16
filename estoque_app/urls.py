from django.urls import path
from estoque_app import views

urlpatterns = [
    # Página inicial
    path("", views.home, name="home"),
    
    # Criar usuário
    path("perfis/", views.perfis, name="perfis"),
    
    # Editar usuário (rota dinâmica com ID do usuário)
    path("editUser/<int:user_id>/", views.edit_user, name="editUser"),
    
    # Remover usuário (rota dinâmica com ID do usuário)
    path("deleteUser/<int:user_id>/", views.delete_user, name="deleteUser"),

     path("produtos/", views.produtos, name="produtos"),

     path("cadastro/", views.signup, name="cadastro"),

     path("login/", views.login, name="login"),
]
