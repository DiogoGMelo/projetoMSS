from django.urls import path
from estoque_app import views

urlpatterns = [
    # Página inicial
    path("", views.home, name="home"),
    
    # Criar usuário
    path("createUser/", views.create_user, name="createUser"),
    
    # Editar usuário (rota dinâmica com ID do usuário)
    path("editUser/<int:user_id>/", views.edit_user, name="editUser"),
    
    # Remover usuário (rota dinâmica com ID do usuário)
    path("deleteUser/", views.delete_user, name="deleteUser"),

    path("showUsers/", views.show_users, name="showUsers"),
]
