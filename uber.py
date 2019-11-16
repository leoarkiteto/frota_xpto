import json

print('''
[1] - NOVO USUARIO
[2] - ACESSO SISTEMA
''')
acesso = int(input())

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

def validarUsuario():
    login()
    verLista()

###### [USUARIO/ADMINISTRADOR] ######
if acesso == 1:
   login()
   nome = login()
