import matplotlib.pyplot as plt 
import networkx as nx
import time
import random
import numpy as np

# Affiche les règles
print("Nombres de joueurs maximum : 2 ",
          "\nLe premier joueur dispose de 3 pions blancs placés sur les cases 0,1,3."
          "\nLe deuxième joueur d'un seul pion noir placé sur la case 5."
          "\nLe joueur avec les pions blancs commence toujours."
          "\nChaques pions se deplacent d'une case à la fois."
          "\nLes pions blancs se déplacent de gauche à droite ou en avant mais jamais en arrière."
          "\nLe pion noir peut se déplacer dans toutes les directions."
          "\nLa partie se termine si le pion noir est bloqué par les pions blancs donc les pions blancs gagnent."
          "\nOu le pion noir gagne s'il passe derrière les pions blancs ou il est hors de portée des pions blancs ou que les déplacements se répètent indéfinément.")

# Variable permettant d'initialiser le jeu
modeDeJeu=int(input("Choisissez un mode de jeu: 0:JcJ / 1: J(Blanc)cIA / 2: J(Noir) vs IA / 3: IAvsIA : "))
global tourBlanc
tourBlanc = True
memoireDerniersMouvements = []
3

#Tableau de base
tableau={0:"B",1:"B",2:"S",3:"B",4:"S",5:"N",6:"S",7:"S",8:"S",9:"S",10:"S"}

#Possibilités de mouvement pour le pion noir et les pions blancs du temps, on essaiera d’aborder la question d’obtenir une strat ́egie optimale ou du moins d’utiliser la superiorite 
dicoMoveNoir={0:[1,2,3], 1:[0,2,4,5], 2:[0,1,3,5], 3:[0,2,5,6], 4:[1,5,7], 5:[1,2,3,4,6,7,8,9], 6:[3,5,9], 7:[4,5,8,10], 8:[5,7,9,10], 9:[5,6,8,10], 10:[7,8,9]}
dicoMoveBlanc={0:[1,2,3], 1:[2,4,5], 2:[1,3,5], 3:[2,5,6], 4:[5,7], 5:[4,6,7,8,9], 6:[5,9], 7:[8,10], 8:[7,9,10], 9:[8,10], 10:[]}
def invert(a):
  return (a[1],a[0])
def checkRepeating():
  for i in range(len(memoireDerniersMouvements)):
    rollingDerniersMouvements = memoireDerniersMouvements
    if len(rollingDerniersMouvements) >=4:    
      if rollingDerniersMouvements[0]==invert(rollingDerniersMouvements[2]) and rollingDerniersMouvements[1]==invert(rollingDerniersMouvements[3]):
        print("Les blancs ont gagné! Répétition")
        return True
  return False
def checkWinBlanc():
  '''Fonction permettant de regarder si les pion blancs ont gagné.'''
  for i in range(11):
    if tableau[i]=="N": noirPos = i
  listePossibleMoveNoir = {0:[1,2,3], 1:[0,2,4,5], 2:[0,1,3,5], 3:[0,2,5,6], 4:[1,5,7], 5:[1,2,3,4,6,7,8,9], 6:[3,5,9], 7:[4,5,8,10], 8:[5,7,9,10], 9:[5,6,8,10], 10:[7,8,9]}[noirPos]
  for y in listePossibleMoveNoir:
    if tableau[y]=="S":
      return False
  print("Les Blancs ont gagné!")
  return True
  
def checkWinNoir():
  '''Fonction permettant de regarder si le pion noir a gagné.'''
  blancPos=[]
  for i in range(11):
    if tableau[i]=="N": 
      noirPos = i
    elif tableau[i]=="B":
      blancPos.append(i)
  if noirPos==0:
    print("Le Noir a gagné!")
    return True
  elif noirPos in [1,2,3]:
    for i in range(3):
      if blancPos[i] in [1,2,3,0]:
        return False
    print("Le Noir a gagné!")
    return True
  elif noirPos in [4,5,6]:
    for i in range(3):
      if blancPos[i] in [0,1,2,3,4,5,6]:
        return False
    print("Le Noir a gagné!")
    return True
    
def move(number, target):
  '''Procédure principale : permet de bouger un pion en fonction des possibilités contenues dans dicoMoveNoir et dicoMoveBlanc.'''
  couleur = tableau[number]
  global tourBlanc
  if(couleur=="N"):
    if(tourBlanc==False):   
      if(target in {0:[1,2,3], 1:[0,2,4,5], 2:[0,1,3,5], 3:[0,2,5,6], 4:[1,5,7], 5:[1,2,3,4,6,7,8,9], 6:[3,5,9], 7:[4,5,8,10], 8:[5,7,9,10], 9:[5,6,8,10], 10:[7,8,9]}[number]):
        if(tableau[target]=="S"):
          tableau[target]=couleur
          tableau[number]="S"
          tourBlanc = True
          if len(memoireDerniersMouvements)>=10:
            memoireDerniersMouvements.append((number,target))
          else:
            memoireDerniersMouvements.pop(0)
            memoireDerniersMouvements.append((number,target))
          return 1
        else:
          print("Case Occupée Noir", number, target)
      else:
        print("Mouvement Impossible")
    else:
      print("Mouvement Impossible: Tour Blanc")
  elif(couleur=="B"):
    if(tourBlanc==True):
      if(target in {0:[1,2,3], 1:[2,4,5], 2:[1,3,5], 3:[2,5,6], 4:[5,7], 5:[4,6,7,8,9], 6:[5,9], 7:[8,10], 8:[7,9,10], 9:[8,10], 10:[]}[number]):
        if(tableau[target]=="S"):
          tableau[target]=couleur
          tableau[number]="S"
          tourBlanc= False
          if len(memoireDerniersMouvements)<=10:
            memoireDerniersMouvements.append((number,target))
          else:
            memoireDerniersMouvements.pop(0)
            memoireDerniersMouvements.append((number,target))
          return 1
        else:
          print("Case Occupée Blanc", number, target)
      else:
        print("Mouvement Impossible")
    else:
      print("Mouvement Impossible: Tour Noir")
  else:
    print("Case Vide") 

#Structure du tableau
DG = nx.Graph()
DG.add_edge(0, 1)
DG.add_edge(0, 2)
DG.add_edge(0, 3)
DG.add_edge(1, 4)
DG.add_edge(1, 5)
DG.add_edge(1, 2)
DG.add_edge(2, 5)
DG.add_edge(2, 3)
DG.add_edge(3, 5)
DG.add_edge(3, 6)
DG.add_edge(4, 7)
DG.add_edge(4, 5)
DG.add_edge(5, 6)
DG.add_edge(5, 7)
DG.add_edge(5, 8)
DG.add_edge(5, 9)
DG.add_edge(6, 9)
DG.add_edge(7, 8)
DG.add_edge(7, 10)
DG.add_edge(8, 9)
DG.add_edge(8, 10)
DG.add_edge(9, 10)

#Crée un arrangement de positions des points en fonctions des liens qu'on vient de définir 
pos = nx.spring_layout(DG, seed=100)

#Affiche les noms des points
nx.draw_networkx_labels(DG, pos)

#Affiche le graphe2
nx.draw(DG, pos)

#Rend la fenêtre interactive et permet de l'animer
plt.ion()

#Loop de jeu
while checkWinBlanc()!=True and checkWinNoir()!=True and checkRepeating()!=True:
    #Dessine chaque point
    for i in range(11):          
            if tableau[i]=="B":
                nx.draw_networkx_nodes(DG, pos, nodelist=[i], node_color="#ffffff")
            elif tableau[i]=="N":
                nx.draw_networkx_nodes(DG, pos, nodelist=[i], node_color="#262626")
            elif tableau[i]=="S":
                nx.draw_networkx_nodes(DG, pos, nodelist=[i], node_color="tab:blue")
    if modeDeJeu==0:
      #Le joueur choisit son action
      pointChoisi = int(input("Point à déplacer : "))
      targetChoisi = int(input("Point où aller : "))
      #On effectue l'action
      move(pointChoisi, targetChoisi)
    if modeDeJeu==3:
      blancPos=[]
      for i in range(11):
        if tableau[i]=="N": 
          noirPos = i
        elif tableau[i]=="B":
          blancPos.append(i)
      if(10 in blancPos):
        blancPos.remove(10)
      if(tourBlanc):
        choix = random.choice(blancPos)
        possibilites={0:[1,2,3], 1:[2,4,5], 2:[1,3,5], 3:[2,5,6], 4:[5,7], 5:[4,6,7,8,9], 6:[5,9], 7:[8,10], 8:[7,9,10], 9:[8,10], 10:[]}[choix]
        choixDir = random.choice(possibilites)
        while move(choix,choixDir)!=1:
          choix = random.choice(blancPos)
          possibilites={0:[1,2,3], 1:[2,4,5], 2:[1,3,5], 3:[2,5,6], 4:[5,7], 5:[4,6,7,8,9], 6:[5,9], 7:[8,10], 8:[7,9,10], 9:[8,10], 10:[]}[choix]
          choixDir = random.choice(possibilites)
        tourBlanc = False
      else:
        choix = noirPos
        possibilites={0:[1,2,3], 1:[0,2,4,5], 2:[0,1,3,5], 3:[0,2,5,6], 4:[1,5,7], 5:[1,2,3,4,6,7,8,9], 6:[3,5,9], 7:[4,5,8,10], 8:[5,7,9,10], 9:[5,6,8,10], 10:[7,8,9]}[choix]
        for i in possibilites:
          if(i in blancPos): possibilites.remove(i)
        choixDir=random.choice(possibilites)
        while move(choix,choixDir)!=1:
          choixDir = random.choice(possibilites)
        tourBlanc = True
    if modeDeJeu==1:
      blancPos=[]
      for i in range(11):
        if tableau[i]=="N": 
          noirPos = i
        elif tableau[i]=="B":
          blancPos.append(i)
      if(10 in blancPos):
        blancPos.remove(10)
      if(tourBlanc):
        pointChoisi = int(input("Point à déplacer : "))
        targetChoisi = int(input("Point où aller : "))
        move(pointChoisi, targetChoisi)
      else:
        choix = noirPos
        possibilites={0:[1,2,3], 1:[0,2,4,5], 2:[0,1,3,5], 3:[0,2,5,6], 4:[1,5,7], 5:[1,2,3,4,6,7,8,9], 6:[3,5,9], 7:[4,5,8,10], 8:[5,7,9,10], 9:[5,6,8,10], 10:[7,8,9]}[choix]
        for i in possibilites:
          if(i in blancPos): possibilites.remove(i)
        choixDir=random.choice(possibilites)
        while move(choix,choixDir)!=1:
          choixDir = random.choice(possibilites)
    if modeDeJeu==2:
      blancPos=[]
      for i in range(11):
        if tableau[i]=="N": 
          noirPos = i
        elif tableau[i]=="B":
          blancPos.append(i)
      if(10 in blancPos):
        blancPos.remove(10)
      if(tourBlanc):
        choix = random.choice(blancPos)
        possibilites={0:[1,2,3], 1:[2,4,5], 2:[1,3,5], 3:[2,5,6], 4:[5,7], 5:[4,6,7,8,9], 6:[5,9], 7:[8,10], 8:[7,9,10], 9:[8,10], 10:[]}[choix]
        choixDir = random.choice(possibilites)
        while move(choix,choixDir)!=1:
          choix = random.choice(blancPos)
          possibilites={0:[1,2,3], 1:[2,4,5], 2:[1,3,5], 3:[2,5,6], 4:[5,7], 5:[4,6,7,8,9], 6:[5,9], 7:[8,10], 8:[7,9,10], 9:[8,10], 10:[]}[choix]
          choixDir = random.choice(possibilites)
        tourBlanc = False
      else:
        #Le joueur choisit son action
        pointChoisi = int(input("Point à déplacer : "))
        targetChoisi = int(input("Point où aller : "))
        #On effectue l'action
        move(pointChoisi, targetChoisi)
    #Pause permet d'animer la fenêtre et de passer à la frame suivante
    plt.pause(0.0001) 
  
#On redessine les points une dernière fois après la fin de la partie
for i in range(11):          
  if tableau[i]=="B":
      nx.draw_networkx_nodes(DG, pos, nodelist=[i], node_color="#ffffff")
  elif tableau[i]=="N":
      nx.draw_networkx_nodes(DG, pos, nodelist=[i], node_color="#000000")
  elif tableau[i]=="S":
      nx.draw_networkx_nodes(DG, pos, nodelist=[i], node_color="tab:blue")
