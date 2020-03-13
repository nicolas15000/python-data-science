""" 
    Loi géométrique ou de pascal - Python géométric law with numpy

    https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.random.geometric.html


 """

 # Import des librairies
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Problème : 
"""  
Les produits fabriqués par une machine ont un taux de défectueux de 3%. 

Quelle est la probabilité que les premiers oc-curs défectueux du cinquième élément soient inspectés?

"""

result = np.random.geometric(p=0.03, size=1000)
print(result);

#   Dans ce tableau, on a obtenu un 1 au deuxième lancer, puis au 19 ème lancer, puis au 3ème lancer etc ...

""" [ 2 19  3  2  2  1  2  1 22  3  1  6  3  1  2 11  8 28  4  7  9  3  3  5
 18  8  2 15  6  4  4 25  3  2  2  3  4  3  3  4  7  9  2 10  1  1  6  7
  5  3  1 10  3  6  1  7  7  1 13  3  2  5  2  7  3  6 10  1  6  5  1 10
  1  1  2  3  4 10  2  4  7  6  6  2  1  3  6  7  2  3 15  7  4 10  4  5
  2 10  5 23] """

# Essayons désormais de voir le pourcentage de malchance d'obtenir un produitr defectueux au bout de la 5 ème fois
result =  (result == 5).sum() / 1000.
print(result * 1000,"%");
