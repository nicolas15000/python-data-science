""" 

On veut calculer le plus court chemin, dans un graphe valué , mais non orienté.

Dans cet exemple, on utilise shortest_path() de la librairie networkX.

Voici les différents algos de distance disponibles avec networkX (Djikstra, Bellman etc ...):
https://networkx.github.io/documentation/stable/reference/algorithms/shortest_paths.html

Source et doc :
https://networkx.github.io/documentation/stable/tutorial.html
https://stackoverflow.com/questions/59894873/networkx-shortest-path-with-condition-on-edges-python

 """


# 0. import des libs
import networkx as nx
import matplotlib.pyplot as plt 

# 1. On crée le graphique , si le graphe est orienté, on utilise G = nx.DiGraph()
G = nx.Graph()

# On ajoute des noeuds
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])

# On ajoute une liste d' arrêtes valuées
G.add_edges_from([('A', 'B', {'marche': 25, 'temps': 300}), ('A', 'C', {'metro': 4, 'temps': 4}), ('A', 'D', {'marche': 3, 'temps': 30}), 
                  ('C', 'E', {'marche': 3, 'temps': 30}), ('D', 'E', {'marche': 3, 'temps': 30}), ('B', 'F', {'marche': 3, 'temps': 30}), 
                  ('D', 'F', {'metro': 4, 'temps': 4}), ('E', 'F', {'marche': 3, 'temps': 30})])

# On affiche notre nombre de noeuds et d' arrêtes valuées
print(G.number_of_nodes())
print(G.number_of_edges())

# On crée notre graphe
nx.draw(G, with_labels=True, font_color='white')

# 2. On trouve les étapes du trajet le plus court de A à F en choississant les valeurs d'arrêtes en temps .

# NOTE : On constate qu'il ne va pas directement de A à B car le temps de est de 300 alors qu'en prenant le raccourci, 
# le temps est plus court , mais on passe par plus de noeuds.

resultat = nx.shortest_path(G, 'A', 'B', weight='temps')

print(resultat)
# Affiche
# ['A', 'D', 'F', 'B']

# On calcule le temps total passé pour aller de A à B
length = nx.shortest_path_length(G, 'A', 'B', weight='temps')

print(length) 
# Affiche le temps total passé ; 64 au lieu de 300 !!! C'est beaucoup  mieux !
# 64

# 3. On imprime le graphique, pour mieux constater les différents chemins..
plt.show()
