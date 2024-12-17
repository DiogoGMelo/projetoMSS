from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from estoque_app.models import User, Seller, Manager


def home(request):
    """
    Método executado quando o usuário está na interface inicial do sistema.
    Envia-se uma solicitação de renderização da interface home.html.
    """
    return render(request, "estoque/home copy.html")


def create_user(request):
    """
    View para criar usuários (Seller ou Manager).
    """
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if not (name and email and password and role):
            return HttpResponse("Todos os campos são obrigatórios.", status=400)

        if role == "seller":
            user = Seller(name=name, email=email, password=password)
            user.save()
        elif role == "manager":
            user = Manager(name=name, email=email, password=password)
            user.save()
        else:
            return HttpResponse("Role inválido.", status=400)

        return redirect("home")  # Redireciona para a página inicial após criar o usuário

    return render(request, "estoque/createUser.html")


def edit_user(request, user_id):
    """
    View para editar as informações de um usuário.
    """
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.name = request.POST.get('name', user.name)
        user.email = request.POST.get('email', user.email)
        if request.POST.get('password'):
            user.password = request.POST.get('password')
        user.save()
        return redirect("home")  # Redireciona para a página inicial após editar o usuário

    return render(request, "estoque/editUser.html", {"user": user})


def delete_user(request):
    """
    View para remover um usuário do sistema.
    """

    if request.method == "POST":
        user = request.POST.get('id')
        try:
            u = User.objects.get(id = user)
            u.delete()

        except User.DoesNotExist:
            return HttpResponse("Usuário não encontrado", status=404)

        return redirect("home")  # Redireciona para a página inicial após deletar o usuário

    return render(request, "estoque/perfis.html")

def perfis (request):
    users = User.objects.all()
    return render(request, "estoque/perfis.html", {"users": users})

def produtos (request):
    return render(request, "estoque/produtos.html")

def signup (request):
    return render(request, "estoque/signup.html")

def login (request):
    return render(request, "estoque/login.html")