#graficas

import matplotlib.pyplot as plt
import numpy as np

x= np.linspace(-5,5,100)
y=x**3
plt.plot(x,y,"g--")
plt.title("f(x) = x^3")
plt.legend("x^3")
plt.grid()
plt.show()



