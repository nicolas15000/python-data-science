# Minimiser le poids d'un mélange sous contrainte d'un resistance
# minimale en fonction de notes x/20 qu'on aurait attribué à chaque élément du mélange.
# La note minimale de la moyenne de la resistance doit être de 12/20
# EN COURS DE RESOLUTION
# Expérimental by Nicolas Estel HULEUX
"""             resistance  poids    
fer :           18/20       16/20        
plastic :       3/20        6/20       
ceramic :       12/20       10/20       
 """

# import PuLP
from pulp import *

# C'est une maximizaiton
prob = LpProblem("Minimize",LpMinimize)

produits = ["fer", "plastic","ceramic"]

resistance = {"fer": 18, "plastic": 3, "ceramic": 12}

poids = {"fer": 16, "plastic": 6, "ceramic": 20}

# Déclarer les variables de décision
x = LpVariable.dicts("produits ", produits , 0)

# Ajouter la fonction objectif
# Minimiser le poids sous contrainte de résistance.
prob += lpSum([poids[i] * x[i] for i in produits ]), "MinimiserPoids"

# Ajouter les contraintes
prob += lpSum([(resistance[i] * x[i]) / 20 for i in produits]) >= 10, "resistance"

# Cette Fonction est nécessaire lorsque les contraintes sont exprimées en %
prob += lpSum([1 * x[f] for f in produits]) == 20, "noteMax"

# On écrit aussi le problem dans un fichier
prob.writeLP ( "opt.lp")

# On utilise le solver pulp
prob.solve()

# On affiche le sstatu de la solution
print ("Status:", LpStatus [prob.status])

# Afficher l'optimium de chaques variables produits qui s'exprime en unité construites
for v in prob.variables ():
    print (v.name, "=", v.varValue)


# Le résultat de la fonctioj objectif est ici :
print ("Note", value (prob.objective /20))
