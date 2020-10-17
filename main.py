import os
from colorama import Fore, init
init(autoreset=True)
def apresentar():
  print(Fore.LIGHTYELLOW_EX + "===== To do List =====\n" + Fore.RESET + "1 --> Inserir uma nova nota\n2 --> Ver todas as notas\n3 --> Excluir uma nota\n4 --> Limpar\n5 --> Copiar lista\n6 --> Alterar arquivo de leitura\n7 --> Sair")
  x = int(input(Fore.LIGHTYELLOW_EX +"Insira sua escolha: "))
  os.system('clear')
  return x

def criar(nome_do_arquivo):
  arq = open(nome_do_arquivo,"a")
  arq.close()

def limpar_nota(nome_do_arquivo, zerar):
  arq = open(nome_do_arquivo,"w") # Cria o arquivo.
  if zerar: #Caso seja True:
    arq.write("Total de notas: 0") #Insere o texto padrão.
  arq.close() #Fecha o arquivo.

def limpar_tela():
  os.system("sleep 2") # Dá um delay antes de continuar;
  os.system("clear") # Limpa o console.

#Criação do arquivo, caso não exista.
criar("notas.txt")
escolha = 0 # Declaração para iniciar o loop.
arquivo = "notas.txt"
while(escolha != 7):
  #Varredura do arquivo
  arq = open(arquivo,"r") # Abro o arquivo em modo leitura
  primeira_linha = arq.readline() # Leio a primeira linha onde contém o total
  try:
    total = int(primeira_linha[16:(len(primeira_linha))]) #Busca o número total de notas, caso não exista um total ele cai no except.
  except:
    limpar_nota(arquivo, True) # Cria o contador iniciando em 0
    total = int(primeira_linha[16:(len(primeira_linha))]) # Passa isso para a varíavel total.
  conteudo = arq.readlines() # Recebe tudo que está abaixo do contador.
  arq.close()
  escolha = apresentar()
  #Funções do menu
  if escolha == 1:
    nota = str(input("Insira sua nota: ")) # Recebo a nota
    limpar_nota(arquivo, False) # Limpo a nota, sem deixar o texto padrão.
    arq = open(arquivo, "a+") # Abro no modo adição no fim.
    total += 1 # Acréscimo no total recebido na rotina de loop.
    arq.write("Total de notas: " + str(total) +"\n") # Inserção do texto padrão com o total atualizado
    if (total-1) > 0: #Prevenção desnecessária.
      arq.writelines(conteudo) # Inserção do conteudo já existente.
    arq.write(str(total) + ". " + nota + "\n") #Inserção da nova nota, mantendo o padrão de entrada.
    arq.close()
    print(Fore.GREEN + "\nNOTA INSERIDA COM SUCESSO") # Feedback ao usuário
    limpar_tela() #Função extra, consulte no slide.
  elif escolha == 2:
    print(Fore.LIGHTYELLOW_EX + "Você tem {} notas\nSuas notas: \n".format(total))
    for i in conteudo:
      print(i)
    input(Fore.LIGHTYELLOW_EX + "Pressione ENTER para continuar.")
    os.system("clear")
  elif escolha == 3:
    print("Você tem {} notas\nSuas notas: \n".format(total)) #Repete a visualização
    for i in conteudo:
      print(i)
    apagador = int(input(Fore.LIGHTYELLOW_EX + "Insira a nota que deseja apagar: ")) # Recebo o índice
    conteudo.pop((apagador-1)) # Apago da lista, com descréscimo, pois a lista começa em 0.
    total-=1 #Decréscimo no total
    limpar_nota(arquivo,False) # Limpo a nota sem a entrada padrão. Consulte "Funções para organização" no slide.
    arq = open(arquivo, "a+") # Abro o arquivo em modo adição no final.
    arq.write("Total de notas: " + str(total) +"\n") #Insiro o novo contador
    contador = 0 #Defino um contador para organizar os elementos
    for i in conteudo: # Loop
      contador+=1 #Acréscimo do contador no começo, pois nossas notas começam em 1.
      arq.write(str(contador) + ". " + (i[3:(len(i))])) #Insiro o contador, o padrão de entrada e,após os 3 primeiros caracteres que são correspondente ao indíce, insiro o conteúdo da nota. Ex: "1. " = 3 caracteres. Por isso o i[3:], ou seja, somente o que está após do índice. 
    arq.close() #Sempre fecha o arquivo que abriu, caso contrário, não será atualizado em tempo real e irá gerar bugs na execução.
    print(Fore.RED + "\nNOTA EXCLUIDA COM SUCESSO") # Feedback para o usuário.
    limpar_tela() # Função de organização.
  elif escolha == 4:
    confirmacao = str(input('Insira "Sim" caso deseje apagar todas as suas notas.\nDigite: ')) #Input de confirmação.
    if confirmacao.lower() == "sim": # Comparação.
      limpar_nota(arquivo, True) # Função de organização.
      conteudo.clear() # Limpeza na lista recebida da rotina de loop.
      total = 0 # Zerar o contador.
      print(Fore.RED + "Notas limpas com sucesso!") # Feedback ao usuário.
      limpar_tela() # Função de organização.
    else:
      print(Fore.LIGHTGREEN_EX + "Suas notas foram mantidas.")
      limpar_tela() # Função de organização.
  elif escolha == 5:
    copia = str(input("Deseja salvar com qual nome: "))
    copia+=".txt"
    criar(copia)
    carq = open(copia, "a+")
    carq.write(primeira_linha)
    carq.writelines(conteudo)
    carq.close()
    limpar_tela()
  elif escolha == 6:
    print("Arquivo lido atualmente: {}".format(arquivo))
    if str(input("Deseja alterar? Caso queira, digite 'Sim'.\nInsira: ")).lower() == "sim":
      arq.close()
      arquivo = ""
      arquivo = str(input("Insira o arquivo que deseja ler: "))
      arquivo+=".txt"
      conteudo.clear()
      primeira_linha = ""
  elif escolha == 7:
    print(Fore.RED + "Programa encerrado!")
    #pass
  else:
    print(Fore.LIGHTRED_EX + "Escolha inválida, tente novamente.")
    limpar_tela()