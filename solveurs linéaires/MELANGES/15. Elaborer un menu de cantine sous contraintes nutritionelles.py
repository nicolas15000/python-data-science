""" 
Traduction et analyse de l'article de Tirthajyoti Sarkar en Français

Minimiser le cout de production du menu d'une école, sous contraintes nutritionelles.


Phase 2 : Analyse et tests du script + passage en français complet.


Source 

https://towardsdatascience.com/linear-programming-and-discrete-optimization-with-python-using-pulp-449f3c5f6e99


"""
import pandas as pd
import pulp
from pulp import *

print ('je suis bien le bon ')
# ON déclare le problème de minimisation.
prob = LpProblem("Je minimise",LpMinimize)

# Lire les premières lignes du fichier EXCEL
# Ne pas lire les contraintes
df = pd.read_excel("datasets/mon-menu-de-cantine.xls",nrows=17)

# Créer une liste des aliments
aliments = list(df['Aliments'])

# Créer un dictionnaire des couts de chaque aliment
costs = dict(zip(aliments,df['Prix/Unitaire']))

# Créer une dictionnaire des calories de chaque aliment
calories = dict(zip(aliments,df['Calories']))

# Créer une dictionnaire du gras total de chaque aliment
gras = dict(zip(aliments,df['Gras (g)']))

# Créer un dictionnaire des carbohydrates de chaque aliment
carbohydrates = dict(zip(aliments,df['Carbohydrates (g)']))

# Créer un dictionnaire des fibres de chaque aliment
fibres = dict(zip(aliments,df['Fibres (g)']))

# Créer un dictionnaire des protéines de chaque aliment
proteines = dict(zip(aliments,df['Proteines (g)']))

# On crée ensuite nos variables
aliments_vars = LpVariable.dicts("aliment",aliments,lowBound=0,cat='Continuous')

# Fonction objectif
prob += lpSum([costs[i]*aliments_vars[i] for i in aliments])

# Les contraintes en calorie
prob += lpSum([calories[f] * aliments_vars[f] for f in aliments]) >= 800.0
prob += lpSum([calories[f] * aliments_vars[f] for f in aliments]) <= 1300.0

# Les contraintes spécifiques
# Gras
prob += lpSum([gras[f] * aliments_vars[f] for f in aliments]) >= 20.0, "grasMinimum"
prob += lpSum([gras[f] * aliments_vars[f] for f in aliments]) <= 50.0, "grasMaximum"

# carbohydrates
prob += lpSum([carbohydrates[f] * aliments_vars[f] for f in aliments]) >= 130.0, "carbohydratesMinimum"
prob += lpSum([carbohydrates[f] * aliments_vars[f] for f in aliments]) <= 200.0, "carbohydratesMaximum"

# Fibres
prob += lpSum([fibres[f] * aliments_vars[f] for f in aliments]) >= 60.0, "fibresMinimum"
prob += lpSum([fibres[f] * aliments_vars[f] for f in aliments]) <= 125.0, "fibresMaximum"

# proteines
prob += lpSum([proteines[f] * aliments_vars[f] for f in aliments]) >= 100.0, "proteinesMinimum"
prob += lpSum([proteines[f] * aliments_vars[f] for f in aliments]) <= 150.0, "proteinesMaximum"


prob.writeLP("problemeCantine.lp")

prob.solve()

# le statut du lp
print ("Status:", LpStatus[prob.status])

# Chaque variable de décision est affichée avec son nom et sa valeur trouvée par l'algo
for v in prob.variables():
     if v.varValue>0:
        print(v.name, "=", v.varValue)



""" 
Status: Optimal
Food_Chocolate_Chip_Cookies = 3.1941723
Food_Frozen_Broccoli = 6.981301
Food__Baked_Potatoes = 0.2059191
 """


