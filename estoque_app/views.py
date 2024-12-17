import sys
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from estoque_app.models import User, Seller, Manager, Product


def home(request):
    """
    Método executado quando o usuário está na interface inicial do sistema.
    Envia-se uma solicitação de renderização da interface home.html.
    """
    return render(request, "estoque/home.html")


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

def signup (request):
    return render(request, "estoque/signup.html")

def login (request):
    return render(request, "estoque/login.html")

def produtos (request):
    stock = Product.objects.all()
    return render(request, "estoque/produtos.html", {"stock": stock})

def registerProduct (request):
    # verifica se a solicitação (request) usa o metodo POST de envio de dados
    if request.method == "POST":        
        product = Product(name=request.POST['name'], price=request.POST['price'], stock_quantity=request.POST['stock_quantity'], description=request.POST['description'])
        product.save()
        return redirect("home")

    return render(request, "estoque/registerProduct.html")

def deleteProduct(request):

    if request.method == "POST":
        product_name = request.POST.get('product_name')
        
        try:
            product = Product.objects.get(name = product_name)
            product.delete()

        except Product.DoesNotExist:
            return HttpResponse(f"Produto {product.name} não encontrado", status=404)
    
    return render(request, "estoque/produtos.html")

def marketplaces (request):
    return render(request, "estoque/marketplaces.html")