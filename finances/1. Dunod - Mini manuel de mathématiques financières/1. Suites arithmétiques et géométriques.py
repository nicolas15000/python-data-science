""" 
Suites arithmétiques et géométriques en python pour la finance :

Sources : 

1. Dunod - Mini manuel de mathématiques financières
2. Yvan Monka - SUITES : Calculer la somme des termes d'une suite (ALGORITHME) - Tutoriel PYTHON """

""" 

Suite arithmétique 
La raison d'une suite arithmétique est r.
U0 est le premier terme, U1 le second ,U2 le troisième et ainsi de suite : Un

Définition globale:
Un + 1 = Un + r 

"""
# -------------------------------------------------------------------------------
# 1. Calculer un terme d'une suite arithmétique si on a u0 ( Le premier terme):
# Un = U0 + n * r
# -------------------------------------------------------------------------------

# Observons un exemple. On veut calculer le terme de rang 5 de la suite arithmétique de premier terme 1 et de raison 2. 
# Autrement dit, on va multiplier 1 par 2, puis ce résultat par 2, etc.

u0 = 1       # on initialise u au premier terme de la suite
n = 5        # on veut calculer le terme de rang 5
raison = 2   # on ajoute 2 à chaque fois.

# Un = U0 + n * r
u5 = 1 + n * raison
print(u5)
# ça nous donne 11 pour le terme de rang 5

# -------------------------------------------------------------------------------
# 2. Calculer la somme des termes d'une suite arithmétique :
# -------------------------------------------------------------------------------

def somme(n):
    u=1
    s=0
    for i in range(0,n+1):
            s=s+u
            u=2+u
           
    return(s)

print(somme(2)) # On itère jusqu'au terme 2
# La somme est de u0+ u1 +u2 = 1 + 3 + 5 = 9

""" Ou avec cette formule  Dunod - Mini manuel de mathématiques financières:
S = ((1er terme + dernier terme) * Nb de terme) / 2 
"""

Ma_somme = ((1 + 5) * 3) / 2
print(Ma_somme)







