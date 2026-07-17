# Desenvolvedor: Kevin Valone Brilhante
# Projeto: IronSave Interactive™
# Descrição: Sistema CRUD para gerenciamento de jogos finalizados
# Data de criação: 13/05/2026
# Última atualização: 17/07/2026

biblioteca = []

titulo = """
  ██╗██████╗  ██████╗ ███╗   ██╗███████╗ █████╗ ██╗   ██╗███████╗
  ██║██╔══██╗██╔═══██╗████╗  ██║██╔════╝██╔══██╗██║   ██║██╔════╝
  ██║██████╔╝██║   ██║██╔██╗ ██║███████╗███████║██║   ██║█████╗  
  ██║██╔══██╗██║   ██║██║╚██╗██║╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  
  ██║██║  ██║╚██████╔╝██║ ╚████║███████║██║  ██║ ╚████╔╝ ███████╗
  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝
"""

dragon = r"""
                                    \||/
                                    |  @___oo
                        /\  /\   / (__,,,,|    
                        ) /^\) ^\/ _)
                        )   /^\/   _)
                        )   _ /  / _)
                    /\  )/\/ ||  | )_)
                   <  >      |(,,) )__)
                    ||      /    \)___)\\
                    | \____(      )___)  )_
                    \______(_______;;; __;;;
"""

from tabulate import tabulate
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "..", "database", "ironsave_database.txt")

line = "=" * 20
line2 = "-" * 50
line3 = "-" * 72

def salvar_arquivo():

    with open(DATABASE, "w", encoding="utf-8") as arquivo:

        for jogo in biblioteca:

            linha = f'{jogo["ID"]};{jogo["Nome"]};{jogo["Plataforma"]};{jogo["Horas"]};{jogo["Nota"]}\n'

            arquivo.write(linha)

def carregar_arquivo():

        with open(DATABASE, "r", encoding="utf-8") as arquivo:

            for linha in arquivo:

                dados = linha.strip().split(";")

                jogo = {

                    "ID": int(dados[0]),
                    "Nome": dados[1],
                    "Plataforma": dados[2],
                    "Horas": float(dados[3]),
                    "Nota": float(dados[4])

                }

                biblioteca.append(jogo)

def cadastrar():

    print("CADASTRAR NOVO JOGO".center(50))
    print(line2)

    while True:

        nome = input("\nInsira o nome do jogo: ").strip()

        if nome == "":
            print("\nO nome não pode ficar vazio ✖")

        elif nome.isdigit():
            print("\nO nome não pode conter apenas números ✖")

        else:
            break

    while True:

        plataforma = input("Insira a plataforma: ").strip()

        if plataforma == "":
            print("\nA plataforma não pode ficar vazia ✖")

        elif plataforma.isdigit():
            print("\nA plataforma não pode conter apenas números ✖")

        else:
            break

    while True:

        try:
            horas = float(input("Insira o total de horas jogadas: "))

            if horas < 0:
                print("\nAs horas não podem ser negativas ✖")

            else:
                break

        except ValueError:
            print("\nDigite apenas números para as horas jogadas ✖")

    while True:

        try:
            nota = float(input("Insira uma nota para o jogo: "))

            if nota < 0 or nota > 10:
                print("\nA nota deve estar entre 0 e 10 ✖")

            else:
                break

        except ValueError:
            print("\nDigite apenas números para a nota ✖")

    id_jogo = len(biblioteca) + 1

    jogo = {
        "ID": id_jogo,
        "Nome": nome,
        "Plataforma": plataforma,
        "Horas": horas,
        "Nota": nota

    }

    biblioteca.append(jogo)

    salvar_arquivo()

    print("\nJogo cadastrado com sucesso ✔")

    input("\nPressione ENTER para retornar ao menu!")

def editar():

    print("EDITAR JOGOS".center(50))
    print(line2)

    if len(biblioteca) == 0:

        print("\nNenhum jogo cadastrado ✖\n")

        input("\nPressione ENTER para retornar ao menu!")

        return menu

    for i, jogo in enumerate(biblioteca, start=1):
        print(i, "►", jogo["Nome"])

    try:
        indice = int(input("\nQual jogo deseja editar?\nJogo: "))

    except ValueError:
        print("\nÍndice inválido ✖")
        input("\nPressione ENTER para retornar ao menu!")
        return

    if indice >= 0 and indice < len(biblioteca):

            novo_nome = input("Novo nome: ")
            nova_plataforma = input("Nova plataforma: ")
            novas_horas = input("Novas horas: ")
            nova_nota = input("Nova nota: ")

            biblioteca[indice]["Nome"] = novo_nome
            biblioteca[indice]["Plataforma"] = nova_plataforma
            biblioteca[indice]["Horas"] = novas_horas
            biblioteca[indice]["Nota"] = nova_nota
            salvar_arquivo()
            print(line2)
            print("Jogo editado com sucesso ✔")

    else:
        print("\nÍndice inválido ✖")
        retornar = input("\nPressione ENTER para retornar ao menu!")  
        if retornar:
           return menu

    
def listar():

    print("BIBLIOTECA DE JOGOS".center(72))
    print(line3)

    if len(biblioteca) == 0:
        print("\nNenhum jogo cadastrado ✖")
        return menu

    tabela = []

    for jogo in biblioteca:

        tabela.append([
            jogo["ID"],
            jogo["Nome"],
            jogo["Plataforma"],
            jogo["Horas"],
            jogo["Nota"]
        ])

        cabecalhos = ["ID", "Nome", "Plataforma", "Horas", "Nota"]

    print("\n")
    print(tabulate(tabela, headers=cabecalhos, tablefmt="rounded_grid"))

    input("\nPressione ENTER para retornar ao menu!")

    return menu

def remover():           
    print("REMOVER JOGOS".center(50))
    print(line2)

    if len(biblioteca) == 0:
        print("\nNenhum jogo cadastrado ✖\n")
        return menu
    else:           

            for i, jogo in enumerate(biblioteca, start=1):
                print(i, "►", jogo["Nome"])
                print(line2)

            try:
                indice = int(input("\nQual jogo deseja remover? \n Jogo: ")) - 1

            except ValueError:
                print("\nDigite um número válido ✖")
                input("\nPressione ENTER para retornar ao menu!")
                return
            
            if indice >= 0 and indice < len(biblioteca):

                biblioteca.pop(indice)
                salvar_arquivo()
                print("\nJogo removido ✔")

            else:
                print("\nÍndice inválido ✖")
                retornar = input("\nPressione ENTER para retornar ao menu!")  
                if retornar:
                    return menu
                
carregar_arquivo()
while True:
    os.system("cls")
    print(titulo)
    print(dragon)
    menu = input('''
                Bem-vindo ao IronSave Interactive™!
==================================================================

[1] Cadastrar
[2] Editar
[3] Listar
[4] Remover
[5] Encerrar o programa
                 
Selecione a opção desejada ➜  ''')
    
    if menu == "1":
        os.system("cls")
        cadastrar()
        
    
    elif menu == "2":
        os.system("cls")
        editar()
        

    elif menu == "3":
        os.system("cls")
        listar()
        

    elif menu == "4":
        os.system("cls")
        remover()
       
    
    elif menu == "5":
        os.system("cls")
        print("\nSistema encerrado!\n")
        break

    else:
        print("Opção inválida!")