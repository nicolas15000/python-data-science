""" 
Les intérêts simples et l'escompte :

Sources : 

1. Dunod - Mini manuel de mathématiques financières
2. Wikibooks : https://fr.wikibooks.org/wiki/Math%C3%A9matiques_avec_Python_et_Ruby/Suites_en_Python
3. https://fr.wikihow.com/calculer-un-int%C3%A9r%C3%AAt-simple

"""

# -------------------------------------
# 1. La formule des intérêts simples .
# -------------------------------------

""" INTERETS PAR ANNEES """
#Les intérêts simples se calculent à partir du capital initial.
#Initialisation des variables :
n = 2     #duree_placement
t = 0.03  #taux_interet annuel de 3 % écrit au format décimal
C0 = 1000 #capital placé

# La somme totale gagnée à l'année n
Cn = C0 * ( 1 + n * t)
print(Cn) # 1060

# Avec une Function :
def placement_annuel(nb_annees,taux_decimal,capital_place):
    return capital_place * (1 + nb_annees * taux_decimal)

print(placement_annuel(2,0.03,1000)) # 1060

# La somme des intérêts sur n années est :
In = n * C0 * t
print(In)
# 60

""" INTERETS PAR MOIS """
# Initialisation des variables :
n = 120     # duree_placement avec un taux mensuel = 10 ans * 12 mois
t = 0.03    # taux_interet MENSUEL de 3 % écrit au format décimal
C0 = 55000  #capital placé

#La somme totale perçue au mois n
Cn = C0 * ( 1 + n * t)
print(Cn)
# 252999

#La somme des intérêts sur n mois est :
In = n * C0 * t
print(In)
# 198 000 euros c'est énorme car c'est un taux mensuel.

""" INTERETS PAR JOURS """
#EXEMPLE 3 : Durée comptée en jours , sur une année comptable de 360 jours.

#Initialisation des variables :
j = 50     #duree_placement en jours
t = 0.02  #taux_interet annuel de 2 % écrit au format décimal
C0 = 1000 #capital placé

# Les intérêts gagnés au bout de 50 jours sont  de (Formule du livre Dunod)
# Ij = C0 * t * (j/360)

somme = C0 * t * (j / 360)
print(somme) # Idem livre Dunod 2.777

# Exemple 4 : Durée comptée en jours(Formule du livre Dunod)

""" ON réalise un placement de 1000 euros à 8% du 1ere mars au 2 septembre .
Le nombre de jours entre ces 2 dates est de 31-1 + 30 +31 +30 + 30 +31 + 31 + 2 = 185 jours """

j = 185     #duree_placement en jours
t = 0.08  #taux_interet annuel de 2 % écrit au format décimal
C0 = 1000 #capital placé

# Le capital au terme du placement est :
# capital = C0 * (1 + t * (j/360))
capital = C0 * (1 + t * (j/360))
print(capital) # Idem livre Dunod 1041.11

# Avec une Function :
def placement_journalier(nb_jours,taux_decimal,capital_place):
    return capital_place * (1 + taux_decimal * (nb_jours/360))

print(placement_journalier(185,0.08,1000)) # Idem livre Dunod 1041.11

# -------------------------------------
# 2. La formule des versements constants .
# -------------------------------------

