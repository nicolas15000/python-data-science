""" 
Un autre problème classique qui peut être modélisé comme un programme linéaire 
concerne le mélange ou le mélange d'ingrédients pour obtenir un produit avec certaines caractéristiques ou propriétés. 
Nous illustrons cette classe avec le problème de déterminer les quantités optimales de trois ingrédients à inclure dans un mélange d'aliments 
pour animaux. Le produit final doit satisfaire à plusieurs restrictions nutritionnelles. 
Les ingrédients possibles, leur contenu nutritif (en kilogrammes de nutriments par kilogramme d'ingrédient) 
et le coût unitaire sont indiqués dans le tableau suivant.

Le mélange doit respecter les restrictions suivantes:

    Calcium - au moins 0,8% mais pas plus de 1,2%.
    Protéines - au moins 22%.
    Fibre - au plus 5%.

Le problème est de trouver la composition du mix alimentaire qui satisfait à ces contraintes tout en minimisant les coûts.

*** Définitions des variables

L, C, S: proportions de farine de calcaire, de maïs et de soja, respectivement, dans le mélange.

*** Contraintes

Le nombre d'heures disponibles sur chaque type de machine est 40 fois le nombre de machines. 
Toutes les contraintes sont dimensionnées en heures. 
Pour la machine 1, par exemple, nous avons 40 heures / machine ¥ 4 machines = 160 heures. 
En écrivant les contraintes, il est habituel de fournir une colonne dans le modèle pour chaque variable.

*** Non négativité

L, C, S > 0

*** Fonction objectif

Étant donné que chaque variable de décision est définie comme une fraction d'un kilogramme, 
l'objectif est de minimiser le coût de la fourniture d'un kilogramme de mélange alimentaire.

Minimiser Z = 10L + 30,5C + 90S


**** RESULTAT CONCORDE AVEC LE DOCUMENT INITIAL ET LES RESULTATS EXCEL !!! OUI OUI OUI ****

Source originelle (EXCEL)

https://www.me.utexas.edu/~jensen/ORMM/models/unit/linear/subunits/blending/index.html




"""

import pulp
from pulp import *

# Liste des ingrédients
Ingredients = ['FARINE','MAIS','SOJA']

# cout d'un ingrédient (cents/kg) 
costs = {
            'FARINE': 10.0, 
            'MAIS': 30.5,
            'SOJA':90.0
        }

# grammes de calcium  (kg/kg) 
calcium = {
            'FARINE': 0.38, 
            'MAIS': 0.001,
            'SOJA':0.002
              }

# grammes de protéines (kg/kg) 
protein = {
            'FARINE': 0.0, 
            'MAIS': 0.09,
            'SOJA':0.50
            }

# grammes de fibres (kg/kg) 
fiber = {
            'FARINE': 0.0, 
            'MAIS': 0.02,
            'SOJA':0.08
            }


# On veut minimiser nos couts
prob = LpProblem("Probleme alimentaire", LpMinimize)

# On se sert du dictionnaire Ingredients pour créer nos variables
ingredient_vars = LpVariable.dicts("Ingr",Ingredients,0)

# Notre function objectif s'exprime en euros ou en dollars
prob += lpSum([costs[i]*ingredient_vars[i] for i in Ingredients]), "Cout total des ingrédients par boite de conserve de 1kg"

# La production totale est de 1 kg
prob += lpSum([ingredient_vars[i] for i in Ingredients]) == 1 ,"conservation"

# On spécifie au solveur PULP Nos contraintes de qualité pour ne pas créer un paté de mauvaise qualité ...
prob += lpSum([calcium[i]    * ingredient_vars[i] for i in Ingredients]) >= 0.008, "calciumRequirementMin"
prob += lpSum([calcium[i]    * ingredient_vars[i] for i in Ingredients]) <= 0.012, "calciumRequirementMax"
prob += lpSum([protein[i]    * ingredient_vars[i] for i in Ingredients]) >= 0.22,  "proteinRequirementMin"
prob += lpSum([fiber[i]      * ingredient_vars[i] for i in Ingredients]) <= 0.05,  "fiberRequirementMax"

# POSSIBILITE Utilisation minimale en g par element
# for p in Ingredients:
#    prob += ingredient_vars[p] >= 10, f"min  for product {p}"


prob.writeLP("problemAlimentaire.lp")
prob.solve()
# le statut du lp
print ("Status:", LpStatus[prob.status])

# Chauqe variable de décision est affichée avec son nom et sa valeur trouvée par l'algo
for v in prob.variables():
    print (v.name, "=", v.varValue)

# Le résultat de la fonction objectif :
print ("Cout total des ingrédients par boite de conserve de 1kg = ", value(prob.objective), "Centimes")


""" 
Status: Optimal
Ingr_FARINE = 0.028170826
Ingr_MAIS = 0.64857216
Ingr_SOJA = 0.32325701
Cout total des ingrédients par boite de conserve de 1kg =  49.15629004

 """


