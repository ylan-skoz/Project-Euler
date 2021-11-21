import math 
import tools

result = 0


for x in range(1000):
    for y in range(1000):
        if tools.isPalindrome(x*y) and x*y > result:
            result = x*y

print(result)