""" 
Chaines de markov à 2 états  :

On veut avoir des prévisions des déménagements, en fonction du nombre d'états dans le temps .

Source : 
Youtube PROMATH
https://www.youtube.com/channel/UC2flwAftkypBx2gLIamxwqg/videos



https://stackoverflow.com/questions/52490184/raising-a-matrix-to-the-nth-power

 """

# 1. On charge la librairie
import numpy as np
from scipy.linalg import logm, expm

# 2. On crée la matrice de transition

""" 
pb déménagement de Lausanne à Lausanne : 0.8 
pb déménagement  de Lausanne à Genève  : 0.2 
pb déménagement  de à Genève à Lausanne: 0.1 
pb déménagement  de à Genève à Genève : 0.9  
"""

""" 

CE CODE NE FONCTIONNE PAS, LE NP POWER NE DONNE PAS LA BONNE MATRICE DE TRANSITION ELEVEE AU CUBE CEST PAS CORRECT, je ne sais pas pourquoi  !
transition_matrix = np.array([[0.8,0.2], 
[0.1,0.9]])
transition_matrix_cube = np.power(transition_matrix, 3)
print(transition_matrix_cube) 

"""


transition_matrix = [[0.8,0.2], [0.1,0.9]]

def matrixMul(a, n):
    if(n <= 1):
        return a
    else:
        return np.matmul(matrixMul(a, n-1), a)

transition_matrix_power = matrixMul(transition_matrix,3)
print(transition_matrix_power )

# 3. On crée le vecteur initial de probabilités de l'état initial
# 20% de la popuplation est sur Lausanne et 80% sur Genève, on peut aussi le mettre n personnes

probabilite_0 = np.array([2000,8000]) 

# 4. On calcule les probabilités de l'état du système en fonction du nombre de temps.

""" 
Etat du système après une période de temps  = P1 = probabilité_0 . transition_matrix
Etat du système après 2 période de temps  = P2 = probabilité_0 . transition_matrix ** 2
Etat du système après 3 période de temps  = P3 = probabilité_0 . transition_matrix ** 3 
Etat du système après n période de temps  = Pn = probabilité_0 . transition_matrix ** n
"""

c = np.dot(probabilite_0,transition_matrix_power) 

print(c)
# [2876. 7124.]