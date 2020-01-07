"""
Usine de jouets

Une entreprise manufacture quatre jouets qui lui apportent des profits de 8,12,14 et 16 euros respectivement. 
Pour se faire, elle utilise 3 matières premières Plastique,Bois et Acier dont elle dispose en stock 42,17,24 kgs. 
Les ressources consommées pour fabriquer une unité de chacun de ces produits sont données dans le tableau ci-dessous. 
L’entreprise souhaite maximiser son profit.

Notons xi la quantité cherchée du produiti.

                automobile    cycle1      cycle2        dragon     nounours    poupee      arc                                stock  
Plastique           2           4           5           7           1           4           2                                  142

Bois                1           1           2           2           1           5           1                                  117

Acier               1           2           3           3           2           2           5                                  124

bénéfice            8           12          14          16          9           13          12



"""

# Import the PuLP lib
from pulp import *

# Create the problem variable
prob = LpProblem ("MaximiserProfit", LpMaximize)



# La liste de nos produits
produits = ["automobile", "cycle1","cycle2","dragon","nounours","poupee","arc"]


# Les bénéfices en EUROS par produits
benefices = {"automobile": 8, "cycle1": 12, "cycle2": 14,"dragon": 16,"nounours":9,"poupee":13,"arc":12}


# Emplois
plastique = {"automobile": 2, "cycle1": 4, "cycle2": 5,"dragon": 7,"nounours":1,"poupee":4,"arc":2}
bois      = {"automobile": 1, "cycle1": 1, "cycle2": 2,"dragon": 2,"nounours":1,"poupee":5,"arc":1}
acier     = {"automobile": 1, "cycle1": 2, "cycle2": 3,"dragon": 3,"nounours":2,"poupee":2,"arc":5}

# ne fonctionne pas
emplois  = {
            0:    [2.0, 4.0, 5.0, 7.0 , 1.0, 4.0, 2.0],
            1:    [1.0, 1.0, 2.0, 2.0 , 1.0, 5.0, 1.0],
            2:    [1.0, 2.0, 3.0, 3.0 , 2.0, 2.0, 5.0]
            }

# Les noms de nos ressources
ressources = {"plastique", "bois", "acier"}

# Les stocks de nos ressources en KG
stocks = {"plastique": 142, "bois ": 117, "acier": 124}

# Problem variables 
x = LpVariable.dicts("produits ", produits , 0)

# Maximiser la quantité de produits et profit.
prob += lpSum([benefices[i] * x[i] for i in produits ]), "MaximiserBenefice"


# On respecte notre production sous contrainte de stocks

prob += lpSum([plastique[i] * x[i] for i in  produits]) <= 142 ,"MaxPlastique"
prob += lpSum([bois[i]      * x[i] for i in  produits]) <= 117 ,"MaxBois"
prob += lpSum([acier[i]     * x[i] for i in  produits]) <= 124 ,"MaxAcier"


# Minimum de production Ne fonctionne pas !
prob += lpSum([x[i] for i in produits]) >= 10 ,"MinProdObjs"

# On écrit aussi le problem dans un fichier
prob.writeLP ( "MeublesModel.lp")

# On utilise le solver pulp
prob.solve()

# On affiche le sstatu de la solution
print ("Status:", LpStatus [prob.status])

# Afficher l'optimium de chaques variables produits qui s'exprime en unité construites
for v in prob.variables ():
    print (v.name, "=", v.varValue)


# Le résultat de la fonctioj objectif est ici :
print ("TotalProfit", value (prob.objective))