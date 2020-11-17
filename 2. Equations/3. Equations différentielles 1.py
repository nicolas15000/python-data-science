""" Equation différentielle 
Sources :
https://www.codingame.com/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/resolution-numerique-dequations-differentielles
https://dridk.me/equation-differentielle.html
https://dridk.me/category/informatique.html
https://interstices.info/modeliser-la-propagation-dune-epidemie/
https://web.stanford.edu/class/archive/math/math21/math21.1156/files/21/notes5.pdf
https://www6.versailles-grignon.inrae.fr/ecosys/content/download/5545/68104/version/1/file/Equations_Differentielles.pdf
https://fr.wikipedia.org/wiki/%C3%89quations_de_pr%C3%A9dation_de_Lotka-Volterra


exemple Eq diff classique : 
différentielle = nombre * f(x) - un nombre
ou 
f'(x) = 3*f(x)-5
"""

# Exemple 1 : équation différentielle d'ordre 1
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# On précise notre constante
a=-0.1
# On crée la liste des temps : 1000 points entre t=0 et t=50. 
# Plus on met de points plus la résolution sera précise
temps = np.linspace(0, 50,1000)

# L'équation différentielle sous forme de fonction :
def equation(Y,temps):
    return a*Y

#On résout notre équation différentielle et on récupère la liste des résultats
Y=odeint(equation, [10], temps)

#On affiche le résultat des Y en fonction du temps
plt.plot(temps,Y)
# On montre le résultat
plt.show()
