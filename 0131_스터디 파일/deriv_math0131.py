import math
import time

def f(x):
    return x**2 + 2*x + 1

def pre_f(f,x,h=0.001):
    return (f(x+h)-f(x))/h
start = time.time()
x_array = range(6)
deriv = [pre_f(f,x) for x in x_array]
end = time.time()
print(deriv)
print(end-start,'sec')
