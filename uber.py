import json

###### [MODULAÇÃO DO SISTEMA] ######

def iniciar():  #FUNCAO DA PAGINA HOME
    print("[1] - NOVO USUARIO \t[2] - ACESSO SISTEMA")
    acesso = int(input())
    return acesso

def login():    #FUNCAO CRIAR LOGIN
    nome = input("login: ")
    senha = input("password: ")
    perfil = "{}, {}".format(nome, senha)
    return perfil

def validarLogin(infoUsuario):  #FUNCAO VALIDAR LOGIN
    baseDados = open("login", "r")
    loginBD = "".join(baseDados.readlines())
    baseDados.close()
    validar = loginBD.find(infoUsuario)
    return validar

def criarLogin(infoUsuario):    #FUNCAO SALVAR LOGIN
    baseDados = open("login", "a")
    baseDados.write(infoUsuario + "\n")
    baseDados.close()
    print("Dados Cadastrados!")

###### [TELA INICIAL: NOVO USUARIO/ACESSO] ######

opcaoInicio = iniciar()
while(opcaoInicio == 1):
    usuario = login()
    validacao = validarLogin(usuario)
    while(validacao != -1):
        usuario = login()
        validacao = validarLogin(usuario)
    cadastro = criarLogin(usuario)
    opcaoInicio = iniciar()
while(opcaoInicio == 2):
    pass
print("Opção Invalida")
