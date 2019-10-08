
# coding: utf-8




import numpy as np
import matplotlib.pyplot as plt




from sklearn.datasets import load_boston

boston = load_boston()




print(boston.DESCR)
print(type(boston))




print(np.array(boston.data[:, 5]))




x = np.array(boston.data[:, 5]) #5 = rooms per house
y = np.array(boston.target)
plt.scatter(x,y, alpha = 0.3)

lenx = np.ones(len(np.array(boston.data[:, 5])))
x = np.array([lenx , x]).T
b = np.linalg.inv(x.T @ x) @ x.T @ y
corte = b[0]
pendiente = b[1]


plt.plot([4,9], [corte+pendiente*4, corte + pendiente*9], c = "red")    #4,9 rango a mostrar linea
plt.show()


