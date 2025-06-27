n = 10001
sieve = []
counter = 2
for _ in range(10001):
    while True:
        if not any(counter % x == 0 for x in sieve):
            sieve.append(counter)
            counter += 1
            break
        counter += 1

print("The solution is " + str(sieve[-1]))