import json


def iniciar():
    print("[1] - NOVO USUARIO \t[2] - ACESSO SISTEMA")
    acesso = int(input())
    return acesso

def login():
    novoUsuario = input("login: ")
    senha = input("password: ")
    naLista = [novoUsuario, senha]
    return naLista

def addLista():
    usuario = open("login", "a")
    usuario.write(str(login()))
    usuario.close()

def verLista():
    listaUsuario = open("login", "r")
    checaUsuario = listaUsuario.readlines()
    listaUsuario.close()
    return checaUsuario

###### [USUARIO/ADMINISTRADOR] ######
start = iniciar()

if(start == 1):
    print("login de cadastro")
elif(start == 2):
    print("login de administrador")
else:
    pi
