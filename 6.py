

import math




sumSquare = 0
squareSum = 0


for i in range (101):
    sumSquare += i**2
    squareSum += i


result = squareSum**2 - sumSquare


print(result)


