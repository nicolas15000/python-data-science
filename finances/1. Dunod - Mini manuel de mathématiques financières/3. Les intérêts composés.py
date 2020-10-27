""" 
Les intérêts composés:

Sources : 

1. Dunod - Mini manuel de mathématiques financières

Functions élaborées à partir des fonctions mathématiques, par NIcolas HULEUX

"""


#1. Les intérêts simples se calculent sur la somme placée initiale, 
#mais les intérêts composés se calculent sur la somme l'année passée.

# Somme initiale investie
S0 = 1000 
# Intérêts en décimal de 5%
i = 0.05
# Durée en années
n = 3 

# Formule : 
# Sn = S0(1+i)**n
# Sn est une suite géométrique de premier terme S0 et de raison (1 + i)

S3 = S0 * (1+i) ** n
print(S3)# La somme dispo au bout de 3 ans est de 1157 , 63 E soit 157,63 Eu d'intérêts


# b/ ReTrouver la valeur placée en connaissant la durée du placement (3) et le taux de placement (0.05) :

valeurPlacee = S3 *(1 + i) ** -n
print(valeurPlacee) # 1000

# c/ Calculer la durée que va mettre un investissement S0 à atteindre une certaine valeur Sn à un taux de i % en décimal.

n = logarithme(n) * ( Sn / S0 ) / logarithme(1 + i)

# Exemple : En combien de temps un capital de 1000 euros peut il atteindre une valeur acquise de 124.51 E au taux annuel de 5 %