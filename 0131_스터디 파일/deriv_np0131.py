import numpy as np
import time
import matplotlib.pyplot as gph

def f(x):
    return x**2 + 2*x +1

x_array = np.linspace(0,5,6)
h = 0.0001
start = time.time()
deriv = (f(x_array + h)-f(x_array)) / h
end = time.time()

print(deriv)
print(end-start)

gph.figure()
gph.plot(x_array, deriv, color = 'red')
gph.grid()
gph.plot(x_array, 2*x_array + 2, color = 'blue')
gph.show()
