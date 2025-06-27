sum = 0
for x in range(limit):
    if x % 3 == 0 or x % 5 == 0:
        sum += x
print("Brute force " + str(sum))