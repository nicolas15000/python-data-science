""" 
Quelles est la probabilité qu'un chien paresseux se lève pour manger (état2) alors qu'il est couché (état 1)  ?

Source : http://www.blackarbs.com/blog/introduction-hidden-markov-models-python-networkx-sklearn/2/9/2017

Les chaines de markov n'ont pas de mémoire des états antérieurs (Memory less). 

"""



""" 
Phase 1 : 
Import des librairies

"""

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


""" 
Phase 2 :

Créer l'espace des états
Créer la probabilité initiale de chaque état . 
35 %, 35 % et 30 %

"""

etats = ['dormir', 'manger', 'defequer']
pi = [0.35, 0.35, 0.3]

espace_etats = pd.Series(pi, index=etats, name='etats')

print(espace_etats)
print(espace_etats.sum())

