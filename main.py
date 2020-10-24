import os
from colorama import Fore, init, Style
from func import iris
init(autoreset=True)


def apresentar(arquivo_atual):
  arquivo_atual = iris(arquivo_atual,False,True)
  #seta = Fore.YELLOW + "-->" + Fore.RESET
  seta = iris("--->",False,True)
  print(Fore.LIGHTYELLOW_EX + "===== " + (Fore.YELLOW + Style.BRIGHT) +"To do List" +(Style.RESET_ALL + Fore.LIGHTYELLOW_EX) +" =====\n" + Fore.RESET + "1 "+ seta +" Inserir uma nova nota\n2 "+ seta +" Ver todas as notas\n3 "+ seta +" Excluir uma nota\n4 "+ seta +" Limpar\n5 "+ seta +" Copiar lista\n6 "+ seta +" Alterar arquivo de leitura\n7 "+ seta + " Remover arquivo\n8 " + seta +" Sair"+ Fore.LIGHTYELLOW_EX + "\n>>> " + (Fore.YELLOW + Style.BRIGHT + arquivo_atual) + (Style.RESET_ALL + Fore.LIGHTYELLOW_EX + " <<<"))
  x = int(input(Fore.LIGHTYELLOW_EX +"Insira sua escolha: "))
  os.system('clear')
  return x

def criar(nome_do_arquivo):
  arq = open(nome_do_arquivo,"w")
  arq.close()

def copiar(arquivo_original, copia):
  arq = open(arquivo_original,"r")
  carq = open(copia,"w+")
  conteudo = arq.readlines()
  carq.writelines(conteudo)
  arq.close() ; carq.close()
  
def limpar_nota(nome_do_arquivo, zerar):
  arq = open(nome_do_arquivo,"w") # Cria o arquivo.
  if zerar: #Caso seja True:
    arq.write("Total de notas: 0") #Insere o texto padrão.
  arq.close() #Fecha o arquivo.

def limpar_tela():
  os.system("sleep 2") # Dá um delay antes de continuar;
  os.system("clear") # Limpa o console.

#Criação do arquivo, caso não exista.
#criar("notas.txt")
escolha = 0 # Declaração para iniciar o loop.
arquivo = "notas.txt"
while(escolha != 8):
  #Varredura do arquivo
  try: 
    arq = open(arquivo,"r") # Abro o arquivo em modo leitura
    primeira_linha = arq.readline()
  except: # Caso não exista ele será criado 
    criar(arquivo)
    limpar_nota(arquivo, True)
    arq = open(arquivo,"r")
    primeira_linha = arq.readline() # Leio a primeira linha onde contém o total
  try:
    total = int(primeira_linha[16:(len(primeira_linha))]) #Busca o número total de notas, caso não exista um total ele cai no except.
  except:
    limpar_nota(arquivo, True) # Cria o contador iniciando em 0
    print(Fore.RED + "Nota foi resetada, falha ao buscar padrão de dados.\n")
    primeira_linha = arq.readline()
    total = int(primeira_linha[16:(len(primeira_linha))]) # Passa isso para a varíavel total.
  conteudo = arq.readlines() # Recebe tudo que está abaixo do contador.
  arq.close()
  escolha = apresentar(arquivo)
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
    print(Fore.LIGHTYELLOW_EX + "Você tem "+ (Fore.RESET + str(total) + Fore.LIGHTYELLOW_EX + " notas") + (Fore.YELLOW + Style.BRIGHT) + "\nSuas notas: \n")
    colorcount = 0
    for i in conteudo:
      if colorcount%2 != 0:
        print(Fore.RESET+i+Fore.RESET)
      else:
        print(Fore.LIGHTGREEN_EX+i+Fore.RESET)
      colorcount+=1
    input(Fore.LIGHTYELLOW_EX + "Pressione" + Fore.YELLOW + " ENTER " + Fore.LIGHTYELLOW_EX + "para continuar.")
    os.system("clear")
  elif escolha == 3:
    print(Fore.LIGHTYELLOW_EX + "Você tem "+ (Fore.RESET + str(total) + Fore.LIGHTYELLOW_EX + " notas") + (Fore.YELLOW + Style.BRIGHT) + "\nSuas notas: \n") #Repete a visualização
    colorcount = 0
    for i in conteudo:
      if colorcount%2 != 0:
        print(Fore.RESET+i+Fore.RESET)
      else:
        print(Fore.LIGHTGREEN_EX+i+Fore.RESET)
      colorcount+=1
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
      limpar_tela()
      if total > 0 and input('Você tem ' + (Fore.RESET) + str(total) + Fore.LIGHTYELLOW_EX +' notas nesse '+ iris('arquivo',False,True) + '.\nInsira ' + Fore.RESET + '"Sim"' + Fore.LIGHTYELLOW_EX + ' caso deseje fazer uma cópia antes de apagar.' + Fore.RESET +'\nDigite: ').lower() == "sim":
        os.system("clear")
        nomedoarq = str(input(Fore.LIGHTYELLOW_EX + "Insira o nome da cópia: ")) + ".txt"
        copiar(arquivo, nomedoarq)
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
    if input("Deseja alterar para a cópia? Caso queira, digite 'Sim'.\nInsira: ").lower() == "sim":
      arq.close()
      arquivo = ""
      arquivo = copia
      conteudo.clear()
      primeira_linha = ""
      print(Fore.GREEN + "Alterado com sucesso!")
      limpar_tela()
    else:
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
      print(Fore.GREEN + "Alterado com sucesso!")
      limpar_tela()
  elif escolha == 7:
    arq.close()
    print(Fore.GREEN + "Arquivos disponíveis: ")
    os.system("ls -a")
    if input(Fore.GREEN + 'Insira ' + Fore.RESET + '"Sim"' + Fore.GREEN + ' caso deseje apagar.' + Fore.RESET +'\nDigite: ').lower() == "sim":
      remover = str(input(Fore.RED + "Insira:"+ Fore.RESET + " "))
      try:
        os.system(("rm "+ remover))
        print(Fore.RED + "\nARQUIVO REMOVIDO")
      except: 
        print(Fore.RED + "Error")
    limpar_tela()
  elif escolha == 8:
    print(Fore.RED + "Programa encerrado!")
    #pass
  else:
    print(Fore.LIGHTRED_EX + "Escolha inválida, tente novamente.")
    limpar_tela()
