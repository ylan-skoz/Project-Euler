

import math


for a in range(1, 1000):
    for b in range(1, 1000):
        calc = (2*a*b/1000)-2*a-2*b+1000
        if calc == 0:
            result = a * b * math.sqrt(a**2 + b**2)
            print(int(result))
            exit()
