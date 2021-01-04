""" 
Le problème de la diète (le régime) de Dantzig.

Ici, La lib Pyomo propose 3 functions permettant diverses functions objectifs.
 
Source : 
https://nbviewer.jupyter.org/github/Pyomo/PyomoGallery/blob/master/diet/DietProblem.ipynb
"""

""" 
Le problème de l'alimentation
Sommaire

L'objectif du problème de régime est de sélectionner des aliments qui satisfont 
les besoins nutritionnels quotidiens à un coût minimum. 
Ce problème peut être formulé sous forme de programme linéaire, 
pour lequel des contraintes limitent le nombre de calories et la quantité de vitamines, 
minéraux, graisses, sodium et cholestérol dans l'alimentation. Danzig (1990) note que le problème de 
l'alimentation a été motivé par le désir de l'armée américaine de minimiser le coût de 
l'alimentation des IG sur le terrain tout en fournissant une alimentation saine.
 """

""" Énoncé du problème

Le problème de l'alimentation peut être formulé mathématiquement comme un problème de programmation 
linéaire en utilisant le modèle suivant.

--> Ensembles

F = ensemble d'aliments
N = ensemble de nutriments

--> Paramètres

ci = coût par portion d'aliment i, ∀i∈F
aij = quantité de nutriment j dans l'aliment i, ∀i∈F, ∀j∈N
Nminj = niveau minimum de nutriment j, ∀j∈N
Nmaxj = niveau maximal de nutriment j, ∀j∈N
Vi = le volume par portion d'aliment i, ∀i∈F
Vmax = volume maximum d'aliments consommés

-->  Variables

xi = nombre de portions de nourriture i à consommer


-->  Objectif

Minimisez le coût total de la nourriture
min ∑i∈Fcixi

-->  Contraintes

Limiter la consommation de nutriments pour chaque nutriment j∈N.
Nminj≤∑i∈Faijxi≤Nmaxj, ∀j∈N

Limitez le volume de nourriture consommée
∑i∈FVixi≤Vmax

Limite inférieure de la consommation
xi≥0, ∀i∈F """


# 1. Importer la lib 

from pyomo.environ import *
infinity = float('inf')

model = AbstractModel()

# 2. Les ensembles F et N sont déclarés de manière abstraite en utilisant le composant Set:
# Nourriture
model.F = Set()
# Nutriments
model.N = Set()

# 3. De même, les paramètres du modèle sont définis de manière abstraite à l'aide du composant Param:

# Cout de chaque nourriture
model.c    = Param(model.F, within=PositiveReals)
# Montant de nutriment pour chaque nourriture
model.a    = Param(model.F, model.N, within=NonNegativeReals)
# Limites inférieure et supérieure de chaque nutriment
model.Nmin = Param(model.N, within=NonNegativeReals, default=0.0)
model.Nmax = Param(model.N, within=NonNegativeReals, default=infinity)
# Volume par portion de nourriture
model.V    = Param(model.F, within=PositiveReals)
# Volume maximum d'aliments consommés
model.Vmax = Param(within=PositiveReals)

