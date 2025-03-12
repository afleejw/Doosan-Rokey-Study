import numpy as np
import matplotlib.pyplot as gph

x_array = np.array([0,1,2,3,4,5])
y_array = 2*x_array**2 + 3*x_array + 1 + np.random.uniform(-10,10,len(x_array))

coeff = np.polyfit(x_array,y_array, deg = 2)
poly_eq = np.poly1d(coeff)

x_fitting = np.linspace(0,5,100)
y_fitting = poly_eq(x_fitting)

gph.scatter(x_array, y_array, color='blue')
gph.plot(x_fitting, y_fitting, color='red')
gph.show()
