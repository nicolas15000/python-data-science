""" 

Source : EICNAM 
U.E : RCP 103 
LA LOI EXPONENTIELLE / LOI CONTINUE


Soit X une variable aléatoire suivant la loi exponentielle de paramètre Λ (se dit "lambda"), 
et a et b deux réels positis ou nuls, alors on a : 

P(X<=a) = 1 - ⅇ ^-Λa
-> Veut dire " La probabilité que la variable aléatoire soies inférieure à a est égale à : 1 - exponentielle ^ -Λ * a.

P(X>=a) = ⅇ ^-Λa
-> Veut dire " La probabilité que la variable aléatoire soies supérieure ou égale  à : exponentielle ^ -Λ * a.

P(a <= X <= b) = ⅇ ^-Λa  - ⅇ ^-Λb
-> Veut dire " La probabilité que la variable aléatoire soies comprise entre a et b est égale  à : exponentielle ^ -Λ * a - exponentielle ^ -Λ * b.

E(x) = 1 / Λ
-> Veut dire l'espérance de la probabilité de x est de 1 divisé par lambda  

La distribution exponentielle est la seule distribution continue qui possède la propriété sans mémoire.

"""

import math

# La durée de vie d'un ordi portable exprimée en années est une variable aléatoire X suivant la loi exponentielle de paramètre Λ = 0.125
# La probabilité que la vie de cet ordi  dépasse 5 ans est :
# p(x > 5) = e^ - 0.125 * 5

pb = math.exp(- 0.125 * 5 )   
print(pb)
# 0.5352614285189903

# La durée de vie d'un ordi portable exprimée en années est une variable aléatoire X suivant la loi exponentielle de paramètre Λ = 0.125
# La probabilité que la vie de cet ordi soit inférieure à 3 ans est :
# p(x < 3) = 1 - e ^ 0.125 * 5

pb = 1 - math.exp(- 0.125 * 3 )   
print(pb)
# 0.31271072120902776

