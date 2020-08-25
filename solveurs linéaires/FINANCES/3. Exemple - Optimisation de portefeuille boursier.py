""" 
** Problème d'optimisation financière 3 .


Il s'agit d'un problème d'optimisation linéaire du risque et du rendement d'un portefeuille. 
Notre objectif est de minimiser le risque du portefeuille tout en satisfaisant simultanément 5 contraintes:

1. La somme des investissements sera de 100 000 $

2. Le portefeuille a un rendement annuel d'au moins 7,5%

3. Au moins 50% des placements sont notés A

4. Au moins 40% des investissements sont immédiatement liquides

5. Les comptes d'épargne et les certificats de dépôt ne dépassent pas 30 000 dollars.

** Source : 
https://towardsdatascience.com/portfolio-linear-optimization-breakdown-f519546ed1ff

https://github.com/ahershy/Linear-Optimization-Portfolio/blob/master/Optimize%20Portfolio.ipynb


** Modélisation du LP :

Pour revoir le processus de résolution d'un problème d'optimisation linéaire, il y a 3 étapes:

1. Variables de décision: ici, il y a 8 variables de décision. Ce sont nos options d'investissement.
    
2. Objectif Fonction: Nous voulons minimiser le risque pour les 8 investissements. 
Voici les placements multipliés par leurs coefficients de risque respectifs.
0X1 + 0X2 + 25X3 + 30X4 + 20X5 + 15X6 + 65X7 + 40X8

3. Contraintes: Enfin, nous voulons définir exactement quelles sont nos contraintes. 
Celles-ci sont exprimées algébriquement ci-dessous dans le même ordre que nous avons énuméré les contraintes précédemment:

1. ΣXi = 100000
2. .04X1+.052X2+.071X3+.1X4+.82X5+.065X6+.2X7+.125X8 >= 7500
3. X1 + X2 + X5 + X7 >= 40000
4. X1 + X3 + X4 + X7 + X8 >= 40000
5. X1 + X2 <= 30000

Au cas où vous seriez confus au sujet des «7 500» de la contrainte n ° 2, ce serait le rendement annuel de 7,5% que nous recherchons multiplié par notre investissement de 100 000 $.


 """