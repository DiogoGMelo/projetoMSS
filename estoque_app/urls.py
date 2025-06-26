from django.urls import path
from estoque_app import views

urlpatterns = [
    # Página inicial
    path("", views.home, name="home"),
    
    # Gerenciar usuários
    path("perfis/", views.perfis, name="perfis"),
    
    # Editar usuário (rota dinâmica com ID do usuário)
    path("editUser/<int:user_id>/", views.edit_user, name="editUser"),
    
    # Remover usuário (rota dinâmica com ID do usuário)
    path("deleteUser/", views.delete_user, name="deleteUser"),

    # Criar usuário
    path("createUser/", views.create_user, name="createUser"),

     # Página produtos
     path("produtos/", views.produtos, name="produtos"),

    # Página para cadastrar usuário na plataforma
     path("cadastro/", views.signup, name="cadastro"),

    # Página para logar usuário na plataforma
     path("login/", views.login, name="login"),

    # Página para cadastrar produto
    path("registerProduct/", views.register_Product, name="registerProduct"),

    # Página de deletar produto
    path("deleteProduct/", views.delete_Product, name="deleteProduct"),

    # Editar usuário (rota dinâmica com ID do usuário)
    path("editProduct/<int:product_id>/", views.edit_product, name="editProduct"),

    # Página de marketplaces
    path("marketplaces/", views.marketplaces, name="marketplaces"),
]
