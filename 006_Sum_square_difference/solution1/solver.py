import math

numbers = range(1, 101)
print("The solution is " + str(int(math.fabs(sum(numbers)**2-sum([n**2 for n in numbers])))))