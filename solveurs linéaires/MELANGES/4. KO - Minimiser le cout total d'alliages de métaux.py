"""
 Industrie minière et métaux

On fabrique de l'acier avec des matières permières, on veut diminuer le cout de la production de cet acier
pour gagner plus d'argent mais , en respectant quand même les caractéristiques minimales d'un acier de qualité

***** NOTE : EN COURS DE CREATION, ACTUELLEMENT FAUX FAUX FAUX ***
****** JE METTRAIS LES LOOPS ENSUITE ******** 

"""

# Minimiser le cout d'alliages de métaux .
# Caractéristiques de l'acier à faire	

""" Elément 	% minimal 	% Max 	
Carbone 	        2 		  3	
Cuivre	            0.4 	 0.6 	
Manganèse	        1.2 	 1.65 

 """
# Caractéristiques, stocks et prix d'achat des alliages			
""" 

Alliage	            C %	    Cu %	Mn %	Stocks kg	Prix €/kg
Alliage de fer 1	2,50	0,00	1,30	4000	    1,20
Alliage de fer 2	3,00	0,00	0,80	3000	    1,50
Alliage de fer 3	0,00	0,30	0,00	6000	    0,90
Alliage de cuivre 1	0,00	90,00	0,00	5000	    1,30
Alliage de cuivre 2	0,00	96,00	4,00	2000	    1,45
Alliage d'alu 1	    0,00	0,40	1,20	3000	    1,20
Alliage d'alu 2	    0,00	0,60	0,00	2500	    1,00 

"""

# Importer la lib PuLP 
from pulp import *

#Créer la variable du problème
prob = LpProblem("MinimiserLpAlliage",LpMinimize)

# Les 7 vars ont une limite en zéro
x1 = LpVariable("Alliage de fer 1",0)
x2 = LpVariable("Alliage de fer 2",0)
x3 = LpVariable("Alliage de fer 3",0)
x4 = LpVariable("Alliage de cuivre 1",0)
x5 = LpVariable("Alliage de cuivre 2",0)
x6 = LpVariable("Alliage d'alu 1",0)
x7 = LpVariable("Alliage d'alu 2",0)


# La fonction objectif est de minimiser le cout total des alliages en EUROS pour une quantité donnée en KGS
prob += 1.20 * x1 + 1.50 * x2 + 0.90 * x3 + 1.30 * x4 + 1.45 * x5 + 1.20 * x6 + 1.00 * x7, "CoutAlliages"

# Contrainte de quantité en KGS .
prob += x1 + x2 + x3 + x4 + x5 + x6 + x7 == 5000, "QuantitéDemandée"

# Contraintes MIN de % de carbone, par alliage
prob += x1 >= 2.5 , "MinCarboneRequirement1"
prob += x2 >= 3    , "MinCarboneRequirement2"
prob += x3 >= 0    , "MinCarboneRequirement3"
prob += x4 >= 0    , "MinCarboneRequirement4"
prob += x5 >= 0    , "MinCarboneRequirement5"
prob += x6 >= 0    , "MinCarboneRequirement6"
prob += x7 >= 0    , "MinCarboneRequirement7"

# Contraintes MIN de % de cuivre, par alliage
prob += x1 >= 0 , "MinCuivreRequirement1"
prob += x2 >= 0 , "MinCuivreRequirement2"   
prob += x3 >= 0.3 , "MinCuivreRequirement3"   
prob += x4 >= 90  , "MinCuivreRequirement4"  
prob += x5 >= 96  , "MinCuivreRequirement5"  
prob += x6 >= 0.4 , "MinCuivreRequirement6"  
prob += x7 >= 0.6 , "MinCuivreRequirement7" 

# Contraintes MIN de % de Manganèse, par alliage
prob += x1 >= 1.3 , "MinManganeseRequirement1"
prob += x2 >= 0.8  , "MinManganeseRequirement2"  
prob += x3 >= 0  , "MinManganeseRequirement3"  
prob += x4 >= 0 , "MinManganeseRequirement4"   
prob += x5 >= 4 , "MinManganeseRequirement5" 
prob += x6 >= 1.2  , "MinManganeseRequirement6"
prob += x7 >= 0  , "MinManganeseRequirement7"

# Contraintes MAX de % de Manganèse, par alliage
prob += x1 <= 1.3 , "MaxManganeseRequirement1"
prob += x2 <= 0.8  , "MaxManganeseRequirement2"  
prob += x3 <= 0  , "MaxManganeseRequirement3"  
prob += x4 <= 0 , "MaxManganeseRequirement4"   
prob += x5 <= 4 , "MaxManganeseRequirement5" 
prob += x6 <= 1.2  , "MaxManganeseRequirement6"
prob += x7 <= 0  , "MaxManganeseRequirement7"


# 5. Contraintes MAX de de stock disponible, par alliage
prob += x1 <= 4000 , "MaxStock"
prob += x2 <= 3000 , "MaxStock1"  
prob += x3 <= 6000  , "MaxStock2"  
prob += x4 <= 5000 , "MaxStock3"   
prob += x5 <= 2000 , "MaxStock4" 
prob += x6 <= 3000  , "MaxStock5"
prob += x7 <= 2500  , "MaxStock6"



# The problem data is written to an .lp file
prob.writeLP("WhiskasModel.lp")

# On utilise le solveur
prob.solve()

# Le statut de la solution
print ("Status:", LpStatus[prob.status])

# On loupe et affiche les optimums de chaque var
for v in prob.variables():
    print (v.name, "=", v.varValue)
    
# Le resultat de la function objectif est ici
print ("Total", value(prob.objective))
