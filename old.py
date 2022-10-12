import matplotlib.pyplot as plt 
import networkx as nx
import time
import random
import numpy as np
from matplotlib.animation import FuncAnimation
tableau = [["B"],["B",0,"B"],[0,"N",0],[0,0,0],[0]]
#Temporaire le temps quon trouve la formule
def index_to_number(index):
  # index = T-uples
  if index == (0,0):
      return 0
  elif index == (1,0):
      return 1
  elif index == (1,1):
      return 2
  elif index == (1,2):
      return 3
  elif index == (2,0):
      return 4
  elif index == (2,1):
      return 5
  elif index == (2,2):
      return 6
  elif index == (3,0):
      return 7
  elif index == (3,1):
      return 8
  elif index == (3,2):
      return 9
  elif index == (4,0):
      return 10
#def update_plot()
# Fonction pour bouger un pion avec sa position index (x,y) et la direction (x,y)
def move(index, dir):
  #Check si la case est vide auquel cas return 0
  if tableau[index[0]][index[1]] == 0:
    print("Case vide")
    return "Case vide"
  else:
    try:
      check = tableau[index[0]+dir[0]][index[1]+dir[1]]
      if(check=="B" or check=="N"):
        print("Case Occupée")
        return "Case Occupée"
      couleur = tableau[index[0]][index[1]]
      tableau[index[0]+dir[0]][index[1]+dir[1]] = couleur 
      tableau[index[0]][index[1]] = 0
      print(index[0],index[1])
      print(dir[0],dir[1])
      print(couleur, index[0]+dir[0], index[1]+dir[1])
    except:
      print("Mouvement impossible")
      return "Mouvement impossible"
#Traduit une direction en coordonees
def direction(dir, index):
  couleur = tableau[index[0]][index[1]]
  if couleur == "B":
    if dir == "Droite" or dir=="droite" or dir=="d" or dir=="D":
      return (0,1)
    elif dir == dir=="Haut" or dir=="haut" or dir=="h" or dir=="H":
      return (1,0)
    else:
      return "Direction non reconnue ou non autorisée"
  elif couleur == "N":
    if dir == dir=="Droite" or dir=="droite" or dir=="d" or dir=="D":
      return (1,0)
    elif dir == dir=="Haut" or dir=="haut" or dir=="h" or dir=="H":
      return (0,1)
    elif dir == dir=="Gauche" or dir=="gauche" or dir=="g" or dir=="G":
      return (-1,0)
    elif dir == dir=="Bas" or dir=="bas" or dir=="b" or dir=="B":
      return (0,-1)
    elif dir == "Haut Droite" or dir=="haut droite" or dir=="hd" or dir=="HD":
      return (1,1)
    elif dir == "Haut Gauche" or dir=="haut gauche" or dir=="hg" or dir=="HG":
      return (-1,1)
    elif dir == "Bas Droite" or dir=="bas droite" or dir=="bd" or dir=="BD":
      return (1,-1)
    elif dir == "Bas Gauche" or dir=="bas gauche" or dir=="bg" or dir=="BG":
      return (-1,-1)
    else:
      return "Direction non reconnue"
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
DG.add_edge(8,9)
DG.add_edge(8, 10)
DG.add_edge(9, 10)
pos = nx.spring_layout(DG, seed=0)
nx.draw_networkx_labels(DG, pos)
nx.draw(DG, pos)
#move((2,1),direction("d",(2,1)))
print(tableau)
#nx.draw_networkx_nodes(DG, pos, nodelist=[5], node_color="#555555")
#nx.draw_networkx_nodes(DG, pos, nodelist=[1,0,3], node_color="#ffffff")
i=0
x=list()
y=list()
plt.ion()
while True:
    for i in range(len(tableau)):
        for y in range(len(tableau[i])):
            
            if tableau[i][y]=="B":
                nx.draw_networkx_nodes(DG, pos, nodelist=[index_to_number((i,y))], node_color="#ffffff")
            elif tableau[i][y]=="N":
                nx.draw_networkx_nodes(DG, pos, nodelist=[index_to_number((i,y))], node_color="#000000")
            elif tableau[i][y]==0:
                nx.draw_networkx_nodes(DG, pos, nodelist=[index_to_number((i,y))], node_color="tab:blue")
    pointChoisiX = int(input("Point à déplacer X"))
    pointChoisiY = int(input("Point à déplacer Y"))
    directionChoisie = input("Direction Choisie")
    move((pointChoisiX,pointChoisiY), direction(directionChoisie,(pointChoisiX,pointChoisiY)))
    print(tableau)
            
    plt.show()
    plt.pause(0.0001) 

