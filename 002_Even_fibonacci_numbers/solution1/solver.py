limit = 4_000_000

a = 0
b = 1
sum = 0

while b < limit:
    if b % 2 == 0:
        sum += b
    a, b = b, a + b

print("Brute force solution: " + str(sum))