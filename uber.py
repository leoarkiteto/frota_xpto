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
if (iniciar() == 1):
    login()
    nome = login()
elif(iniciar() == 2):
    print("OPÇOES DE ADMINISTRADOR")
else:
    print("OPÇÃO INVALIDA, TENTE OUTRA VEZ")
    iniciar()