import math

required_numbers = range(1, 21)
prime_factors = []

def get_prime_factors(n: int) -> list:
    leftovers = n
    res = []
    while leftovers != 1:
        for i in range(2, int(leftovers + 1)):
            if leftovers % i == 0:
                res.append(i)
                leftovers /= i
                break
    return res

for n in required_numbers:
    primes_of_n = get_prime_factors(n)
    pointer = 0
    for p in primes_of_n:
        while True:
            if pointer >= len(prime_factors):
                prime_factors.append(p)
                pointer += 1
                break
            if prime_factors[pointer] == p:
                pointer += 1
                break
            if prime_factors[pointer] > p:
                prime_factors.insert(pointer, p)
                pointer += 1
                break
            pointer += 1

print("The solution is " + str(math.prod(prime_factors)))
