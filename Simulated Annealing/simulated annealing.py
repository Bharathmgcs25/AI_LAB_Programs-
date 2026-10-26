
import random
import math

def f(x):
    return x * x

x = 10.0
best = x
temperature = 100

while temperature > 0.1:
    new_x = x + random.uniform(-1, 1)
    change = f(new_x) - f(x)

    if change < 0:
        x = new_x
    elif random.random() < math.exp(-change / temperature):
        x = new_x

    if f(x) < f(best):
        best = x

    temperature *= 0.95

print("Best x:", round(best, 4))
print("Minimum value:", round(f(best), 4))
