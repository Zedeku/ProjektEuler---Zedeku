import numpy as np

divisors = np.array([3, 5])
limit = 1000

true_divisors = np.array([x for x in divisors if len([y for y in divisors if y % x == 0]) == 1])
sum = 0

for x in true_divisors:
    # Anzahl des Auftretens der Vielfachen
    count = int((limit - 1) / x)
    # Gausssche Summenformel nutzen
    g_sum = count * (count + 1) / 2
    # Mit Vielfacher multiplizieren und abspeichern
    sum += x * g_sum

print("The result is " + str(int(sum)))