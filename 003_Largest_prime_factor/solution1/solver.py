number = 600851475143

limit = int(number**0.5)

def is_prime(n):
    for i in range(2, int((n+1)**0.5)):
        if n % i == 0:
            return False
    return True

if is_prime(number):
    print("Brute force solution: " + str(number))
else:
    for i in reversed(range(1, limit)):
        if number % i == 0 and is_prime(i):
            print("Brute force solution: " + str(i))
            break