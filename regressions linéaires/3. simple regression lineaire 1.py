# https://www.geeksforgeeks.org/linear-regression-python-implementation/

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)
print('predicted response:', y_pred, sep='\n')

axes = plt.axes()
axes.grid() # dessiner une grille pour une meilleur lisibilité du graphe

# LES POINTS DATA DE BASE
plt.scatter(x,y) # X et Y sont les variables qu'on a extraite dans le paragraphe précédent
# La ligne
plt.plot(x,y_pred, color='blue', linewidth=3)

plt.show()