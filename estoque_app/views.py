from datetime import datetime
import random, time
from http import client
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils import timezone
from estoque_app.models import *
# Create your views here.

def home(request):
    #método executado quando o usuário está na interface inicial do sistema. 
    #Envia-se uma solicitação de renderização da interface home.html
    return render(request, "estoque/home.html")

def createUser(request):
    if request.method == "POST":
        match request.POST['role']:
            case "seller":
                user = registerSeller(request)
            case "manager":
                user = registerManager(request)
    else:  
        return render(request, "estoque/createUser.html")


def registerSeller(request):
    seller = Seller(name = request.POST['name'], email = request.POST['email'], password = request.POST['password'])
    seller.createSeller()
    return seller

def registerManager(request):
    manager = Manager(name = request.POST['name'], email = request.POST['email'], password = request.POST['password'])
    manager.createManager()
    return manager