import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 500)
plt.plot(x, np.around(x,0), label="around(x,0)")
plt.plot(x, np.trunc(x), label="trunc(x)")
plt.legend()

plt.show()