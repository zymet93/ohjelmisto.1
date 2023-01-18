import math
import random


Pisteet = int(input("Syötä pisteiden määrä: "))
N = 0
n = 0
while N != Pisteet:
    N += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 < 1:
        n += 1
if N == Pisteet:
    pi = 4 * n / N
    print("Piin likiarvo annetuilla pisteillä: " + str(pi))