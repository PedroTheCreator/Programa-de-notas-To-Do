import os
def iris(texto,balanceado=False,retornar=False):
  from colorama import Fore
  class Cores():
    def __init__(self,cor):
      self.cor = cor
    def mudar_cor(self):
      if self.cor == "RED":
        return(Fore.RED)
      elif self.cor == "YELLOW":
        return(Fore.YELLOW)
      elif self.cor == "LIGHTYELLOW_EX":
        return(Fore.LIGHTYELLOW_EX)
      elif self.cor == "GREEN":
        return(Fore.GREEN)
      elif self.cor == "LIGHTBLUE_EX":
        return(Fore.LIGHTBLUE_EX)
      elif self.cor == "BLUE":
        return(Fore.BLUE)
      elif self.cor == "MAGENTA":
        return Fore.MAGENTA
      elif self.cor == "CYAN":
        return Fore.CYAN
  tamanho = len(texto)
  tamanho = round((tamanho/7))
  lista_cores = ["RED", "YELLOW", "LIGHTYELLOW_EX","GREEN","LIGHTBLUE_EX","CYAN","BLUE","MAGENTA"]
  
  contador = 0
  resultado = ""
  if balanceado == False:
    for i in range(0,len(texto)):
      Iris = Cores(lista_cores[contador])
      resultado = resultado +  Iris.mudar_cor() + str(texto[i])
      contador +=1
      if contador == 8:
        contador = 0  
  else:
    temporaria = tamanho
    for i in range(0,len(texto)):
      Iris = Cores(lista_cores[contador])
      resultado = resultado +  Iris.mudar_cor() + str(texto[i])
      if i > temporaria:
        contador+=1
        temporaria += tamanho
  resultado = resultado + Fore.RESET
  #print(type(retornar))
  #print((retornar))
  if retornar:
    return(resultado)
  else:
    print(resultado)
  
  

def clear():
  os.system("clear")
class Calculadora:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def soma(self):
    print(self.x+self.y)
  def sub(self):
    print(self.x-self.y)
  def mult(self):
    print(self.x*self.y)
  def div(self):
    print(self.x/self.y)
  def poten(self):
    print(self.x**self.y)

def hw():
  print("hello world!")

def laquel():
  return ("Deusa egípcia")

def volume(raio):
  from math import pi
  ve = (4 * pi * (raio ** 3)) / 3
  print("Volume = {0:f}cm³".format(ve))

def secret():
  return "leuqaL ,IIIIIH"

def reverso(texto, retorno):
  texto = str(texto)
  tamanho = len(texto) - 1
  reverso = ""
  for i in range(0, (tamanho + 1)):
    reverso = reverso + texto[tamanho]
    tamanho = tamanho - 1
  if retorno == False:
    print(reverso)
  else:
    return reverso

def vsf():
  print("TOMAR NO CU\nRatomanucu")
def grafico(titulo):
  import PySimpleGUI as sg
  import matplotlib.pyplot as plt
  arqx = open("progress.txt", "a")
  arqx = open("progress.txt", "r")
  temp = arqx.read()
  if temp == '':
    temp = 0
  
  class TelaPython:
    def __init__(self):
      sg.theme('DarkAmber')
      layout = [  # Elementos
        [sg.Text("Projeto: " + titulo)],
        [sg.Text("Status anterior: " + str(temp) + "%")],
        [sg.Text("Status atual"),sg.Slider(range=(0,100),default_value=(float(temp)),orientation='h', size=(20,25))],
        #[sg.Text("Status atual"), sg.Input()],
        [sg.Button('Enviar')],
        [sg.Quit('Mostrar')]
      ]
      self.janela = sg.Window("Dados do Usuário").layout(layout)
      self.button, self.pronto = self.janela.Read()
      #self.Quit, self.mostrarG()
      self.trava = False
    def fechar(self):
      self.janela.close()
    def mostrarG(self):
      self.trava = True
      self.fechar()
      
  
  tela = TelaPython()
  if tela.trava == True:
    pronto = int(temp)
  else:
    pronto = int(tela.pronto[0])  # Recebe os dados do input
    tela.fechar()
  
  print(pronto)
  if pronto > 0 and pronto != None:
    valores_2 = [pronto, (100 - pronto)]  # Relação do gráfico
    arq = open("progress.txt", "w")
    arq.write(str(pronto))
    arq.close()
    plt.xlabel(titulo)
    plt.pie(valores_2, labels=["Pronto", "Faltante"], autopct="%1.0f%%")
    plt.show()
  else:
    arq = open("progress.txt", "w")
    arq.write(str(temp))
    arq.close()
    print("Não foi possível completar")
  
  arqx.close()

class Redutor:
  def __init__(self,idade,nome):
    self.idade = idade
    self.nome = nome 
    self.meses = self.idade*12
    self.semanas = round((self.meses*4.34524)+0.5)
    self.dias = round((self.semanas*7))

def Remgard():
  os.system("clear")
  grafico("Remgard II")
  
def desinstalar():
  from instalador import desinstalar as ds
  ds()

def atualizar():
  from instalador import atualizar
  atualizar()

