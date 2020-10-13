""" 
Les intérêts simples et l'escompte :

Sources : 

1. Dunod - Mini manuel de mathématiques financières
2. Wikibooks : https://fr.wikibooks.org/wiki/Math%C3%A9matiques_avec_Python_et_Ruby/Suites_en_Python
3. https://fr.wikihow.com/calculer-un-int%C3%A9r%C3%AAt-simple

"""

# 1. La formule des intérêts simples .

#Les intérêts simples se calculent à partir du capital initial.

#Initialisation des variables :
n = 2     #duree_placement
t = 0.03  #taux_interet annuel de 3 % écrit au format décimal
C0 = 1000 #capital placé

#La somme totale remboursée à l'année n
Cn = C0 * ( 1 + n * t)
print(Cn)
# 1060

#La somme des intérêts sur n années est :
In = n * C0 * t
print(In)
# 60

#EXEMPLE 2 :
#Initialisation des variables :
n = 120     # duree_placement avec un taux mensuel = 10 ans * 12 mois
t = 0.03    # taux_interet MENSUEL de 3 % écrit au format décimal
C0 = 55000  #capital placé

#La somme totale remboursée au mois n
Cn = C0 * ( 1 + n * t)
print(Cn)
# 252999

#La somme des intérêts sur n mois est :
In = n * C0 * t
print(In)
# 198 000 euros c'est énorme car c'est un taux mensuel.

#EXEMPLE 3 :

