import random

x_array = [i for i in range(6)]
y_array = [2*x**2 + 3*x + 1 + random.uniform(-3,3) for x in x_array]
y_aver = sum(y_array)/len(y_array)
y_pred = [y_aver]*len(x_array)

print(list(zip(x_array,y_array)))
print(sum(y_pred)/len(y_pred))

