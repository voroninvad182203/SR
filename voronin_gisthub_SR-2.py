Задание 1

import math
def function(x):
    return (x ** 3 + x ** 0.5) / (math.exp(x) + math.atan(x)) ** 2


x = 2
arr1 = []

for i in range(20):
    x += 0.05
    arr1.append(function(x))

print(arr1)


Задание 2

a = 0
for i in range(1, 9):
    a += 2 * i / i + 2

print()
print(2 * a / 3)

Задание 3

n=6
print([[i for i in range(1,n+1)] if j%2==0 else [i for i in range(n,0,-1)] for j in range(n)])
