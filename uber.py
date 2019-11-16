import json

print('''
[1] - NOVO USUARIO
[2] - ACESSO SISTEMA
''')
acesso = int(input())

novoUsuario = ""
def login():
    novoUsuario = input("login: ")
    senha = input("password: ")
    naLista = {"nome":novoUsuario, "senha":senha}
    return naLista

def addLista():
    usuario = open("login", "a")
    usuario.write(str(login()))
    usuario.close()


def verLista():
    listaUsuario = open("login", "r")
    checaUsuario = str(listaUsuario.readlines())
    listaUsuario.close()
    if novoUsuario in checaUsuario:
        print("Usuario Existente!!")
        return False
    else:
        addLista()
        return True

###### [USUARIO/ADMINISTRADOR] ######
if acesso == 1:
    login()
    verLista()
#    while (verLista == False):

          

###### [VIATURAS] ######
# modelo = input("MODELO/MARCA: ")
# matricula = input("MATRICULA: ")
# kmRodados = input("KM RODADOS: ")
# valorFaturado = input("VALOR FATURADO (EURO): ")
# numeroServico = input("Nº DE SERVIÇOS: ")

# veiculo = {         #Dicionario propriedade dos veiculos
#     "modelo": modelo,
#     "matricula" : matricula,
#     "kmRodados" : kmRodados,
#     "valorFaturado" : valorFaturado,
#     "numeroServico" : numeroServico,
#     "posicao" : [2.5, 2.5]
#     }

###### [VIATURAS - BASE DE DADOS] ######
# viatura = open("viaturas", "a")
# viatura.write(str(veiculo) + "\n")
# viatura.close



###### [SECAO - ADMINISTRADOR] ######
