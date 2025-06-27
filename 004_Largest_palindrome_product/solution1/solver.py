def is_palindrome(n : int) -> bool:
    f_string = str(n) 
    b_string = f_string[::-1]
    return f_string == b_string

def has_two_three_digit_divisors(n: int) -> bool:
    node = int(n ** 0.5)
    while node >= 100:
        if n % node == 0:
            if n / node < 1000:
                return True
            else:
                return False
        node -= 1
    return False

counter: int = 999**2

while counter >= 100**2:
    if is_palindrome(counter) and has_two_three_digit_divisors(counter):
        print("The solution is " + str(counter))
        exit()
    counter -= 1
print("There is no solution")