#importar funções do Sistema Operacional
import os.path

#Função para registrar um novo jogador no sistema; vitórias e derrotas = 0
def criaNovoJogador():
   nome = input("Digite o nome do novo jogador: ")

#verifica se um arquivo para esse jogador já existe
   if os.path.isfile("{}.txt" .format(nome)):
       print ("Jogador já registrado!\n")
   else:
       print ("Registrando o jogador {}\n" .format(nome))
   f = open("{}.txt" .format(nome) , "w")
   f.write("0\n") #pontuação/vitórias
   f.write("0\n") #derrotas
   f.close()

#Função para excluir um jogador
def excluiJogador():
   nome = input ("Digite o nome do jogador a ser excluído: ")
#Verifica se o jogador a ser excluído existe
   if os.path.isfile("{}.txt" .format(nome)):
       print ("Excluindo o jogador {} \n" .format(nome))
       os.remove("{}.txt" .format(nome))
   else:
       print ("Jogador {} não existe!\n" .format(nome))

#Função para ler a pontuação do jogador
def lePontuacao():
   nome = input("Digite o nome do jogador: ")
#Se o jogador existe, leia a sua pontuação
   if os.path.isfile("{}.txt" .format(nome)):
       f = open ("{}.txt" .format(nome), "r")
       print ("Pontuação de {}: " .format(nome))
       historico = f.readlines() #pego todas as linhas do arquivo para leitura
       vitorias = historico [0]
       derrotas = historico [1]
       print ("Vitórias: {}\n Derrotas: {}" .format(vitorias,derrotas))
   else:
       print("Jogador {} não existe" .format(nome))     

def empate():
 print ("Empate!")

def jogoSupremo():
  #Criando uma matriz
 matriz = [
   [" "," "," "," "," "," "],
   [" "," "," "," "," "," "],
   [" "," "," "," "," "," "],
   [" "," "," "," "," "," "],
   [" "," "," "," "," "," "],
   [" "," "," "," "," "," "]
 ]

 #Imprimindo o jogo para o usuário
 jogadas = 0
 while jogadas <=25:
   tabuleiro = """
    {}  | {} | {} | {} | {}
    ---+---+---+---+---
    {}  | {} | {} | {} | {}
    ---+---+---+---+---
    {}  | {} | {} | {} | {}
    ---+---+---+---+---
    {}  | {} | {} | {} | {}
    ---+---+---+---+---
    {}  | {} | {} | {} | {}
    """.format(matriz[0][0], matriz[0][1], matriz[0][2], matriz[0][3], matriz[0][4],
    matriz[1][0], matriz[1][1], matriz[1][2], matriz[1][3], matriz[1][4],
    matriz[2][0], matriz[2][1], matriz[2][2], matriz[2][3], matriz[2][4],
    matriz[3][0], matriz[3][1], matriz[3][2], matriz[3][3], matriz[3][4],
    matriz[4][0], matriz[4][1], matriz[4][2], matriz[4][3], matriz[4][4])


   print(tabuleiro)
   
   #definindo as jogadas que resultam em vitória para X
   if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X" and matriz[0][3] == "X" or matriz[0][4] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X" and matriz [0][3]:
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X" and matriz[1][3] == "X" or matriz[1][4] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X" and matriz [1][3]:
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X" and matriz[2][3] == "X" or matriz[2][4] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X" and matriz [2][3]:
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[3][0] == "X" and matriz[3][1] == "X" and matriz[3][2] == "X" and matriz[3][3] == "X" or matriz[3][4] == "X" and matriz[3][1] == "X" and matriz[3][2] == "X" and matriz [3][3]:
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[4][0] == "X" and matriz[4][1] == "X" and matriz[4][2] == "X" and matriz[4][3] == "X" or matriz[4][4] == "X" and matriz[4][1] == "X" and matriz[4][2] == "X" and matriz [4][3]:
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()

   if matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X" and matriz[3][0] == "X" or matriz[4][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X" and matriz [3][0]:
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X" and matriz[3][1] == "X" or matriz[4][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X" and matriz [3][1]:
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X" and matriz[3][2] == "X" or matriz[4][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X" and matriz [3][2]:
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][3] == "X" and matriz[1][3] == "X" and matriz[2][3] == "X" and matriz[3][3] == "X" or matriz[4][3] == "X" and matriz[1][3] == "X" and matriz[2][3] == "X" and matriz [3][3]:
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][4] == "X" and matriz[1][4] == "X" and matriz[2][4] == "X" and matriz[3][4] == "X" or matriz[4][4] == "X" and matriz[1][4] == "X" and matriz[2][4] == "X" and matriz [3][4]:
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
  
   #definindo as jogadas que resultam em vitória para O
   if matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O" and matriz[0][3] == "O" or matriz[0][4] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O" and matriz [0][3]:
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O" and matriz[1][3] == "O" or matriz[1][4] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O" and matriz [1][3]:
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O" and matriz[2][3] == "O" or matriz[2][4] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O" and matriz [2][3]:
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[3][0] == "O" and matriz[3][1] == "O" and matriz[3][2] == "O" and matriz[3][3] == "O" or matriz[3][4] == "O" and matriz[3][1] == "O" and matriz[3][2] == "O" and matriz [3][3]:
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[4][0] == "O" and matriz[4][1] == "O" and matriz[4][2] == "O" and matriz[4][3] == "O" or matriz[4][4] == "O" and matriz[4][1] == "O" and matriz[4][2] == "O" and matriz [4][3]:
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()

   if matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O" and matriz[3][0] == "O" or matriz[4][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O" and matriz [3][0]:
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O" and matriz[3][1] == "O" or matriz[4][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O" and matriz [3][1]:
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O" and matriz[3][2] == "O" or matriz[4][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O" and matriz [3][2]:
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][3] == "O" and matriz[1][3] == "O" and matriz[2][3] == "O" and matriz[3][3] == "O" or matriz[4][3] == "O" and matriz[1][3] == "O" and matriz[2][3] == "O" and matriz [3][3]:
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][4] == "O" and matriz[1][4] == "O" and matriz[2][4] == "O" and matriz[3][4] == "O" or matriz[4][4] == "O" and matriz[1][4] == "O" and matriz[2][4] == "O" and matriz [3][4]:
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()

   #Definindo as jogadas que resultam em vitoria para X em diagonais
   if matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X" and matriz[3][3] == "X" or matriz [4][4] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X" and matriz[3][3] == "X":
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][1] == "X" and matriz[1][2] == "X" and matriz[2][3] == "X" and matriz[3][4] == "X":
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[1][0] == "X" and matriz[2][1] == "X" and matriz[3][2] == "X" and matriz[4][3] == "X":
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[1][4] == "X" and matriz[2][3] == "X" and matriz[3][2] == "X" and matriz[4][1] == "X":
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][3] == "X" and matriz[1][2] == "X" and matriz[2][1] == "X" and matriz[3][0] == "X":
     print("Jogador 2 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()

   #Definindo as jogadas que resultam em vitoria para O em diagonais
   if matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O" and matriz[3][3] == "O" or matriz [4][4] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O" and matriz[3][3] == "O":
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][1] == "O" and matriz[1][2] == "O" and matriz[2][3] == "O" and matriz[3][4] == "O":
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[1][0] == "O" and matriz[2][1] == "O" and matriz[3][2] == "O" and matriz[4][3] == "O":
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[1][4] == "O" and matriz[2][3] == "O" and matriz[3][2] == "O" and matriz[4][1] == "O":
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()
   elif matriz[0][3] == "O" and matriz[1][2] == "O" and matriz[2][1] == "O" and matriz[3][0] == "O":
     print("Jogador 1 venceu!")
     print (vitorias())
     print(derrotas())
     print("Pontuação registrada! Voltando para o menu...")
     return main()

   #Criando alteração para X e O
   if (jogadas%2) == 0:
     print("Vez do Jogador 1 (O)")
   else:
     print("Vez do jogador 2 (X)")

   #Criando um looping para fazer jogadas consecutivas
   linha = int(input("Digite a linha que deseja jogar: "))
   coluna = int(input("Digite a Coluna que deseja jogar: "))

   while matriz [linha][coluna] == "X":
       print ("\nJogador anterior ja utilizou esse espaço!\n")
       linha = int(input("Digite a linha desejada:  "))
       coluna = int(input("Digite a coluna desejada:  "))

   while matriz[linha][coluna] == "O":
       print ("\nJogador anterior ja utilizou esse espaço!\n")
       linha = int(input("Digite a linha desejada:  "))
       coluna = int(input("Digite a coluna desejada:  "))

   jogadas +=1 
  
   #diferenciando X de O
   if (jogadas%2) == 0:
     matriz[linha][coluna] = "X"
   else:
     matriz[linha][coluna] = "O"

   if jogadas == 25:
     print(empate())
     return main()

def vitorias():
 nome = input ("Digite o nome do jogador que ganhou a rodada: ")
 f = open("{}.txt".format(nome), "r")
 historico = f.readlines()  #leio o arquivo
 f.close()
 vitorias = int(historico[0]) + 1
 derrotas = int(historico[1])
 f = open("{}.txt".format(nome), "w")
 f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / vitorias
 f.close()

def derrotas():
 nome = input ("Digite o nome do jogador que perdeu a rodada: ")
 f = open("{}.txt".format(nome), "r")
 historico = f.readlines()  #leio o arquivo
 f.close()
 vitorias = int(historico[0])
 derrotas = int(historico[1]) + 1
 f = open("{}.txt".format(nome), "w")
 f.write("{}\n{}".format(vitorias, derrotas))  #pontuação / vitorias
 f.close()

def iniciar():
 nome1=input("Digite o nome do jogador 1: ")
  #verifica se um arquivo para esse jogador já existe
 if os.path.isfile("{}.txt".format(nome1)):
   print  ("{} entrou no jogo!\n".format(nome1))
 else:
   print ("{} não registrado!\n".format(nome1))
   return main()

 nome2=input("Digite o nome do jogador 2: ")
 #verifica se um arquivo para esse jogador já existe
 if os.path.isfile("{}.txt".format(nome2)):
   print  ("{} entrou no jogo!\nVamos começar!\nJogador 1 inicie a rodada:\n".format(nome2))
   pass
 else:
   print  ("{} não registrado!\n".format(nome2))
   return main()
 jogoSupremo()
 #Cria o programa principal
def main():
   while True:
       print("---------Menu---------")
       print ("1 - Criar novo jogador")
       print ("2 - Exibir pontuação")
       print ("3 - Excluir jogador")
       print ("4 - Iniciar o jogo da velha")
       break

#crio uma variável para a escolha do menu
   opcao = input ("Escolha a opção desejada: ")
  
   if opcao == "1":
       criaNovoJogador()
       return main()
   elif opcao == "2":
       lePontuacao()
       return main()
   elif opcao == "3":
       excluiJogador()
       return main()
   elif opcao =="4":
       iniciar()
   else:
       print ("Escolha uma das opções acima apenas!")
       return main()
 
#Execute o programa
main()
