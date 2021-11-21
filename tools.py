
import math

def isPrime(number):

    for i in range(2, number, 2):
        if number % i == 0:
            return False

        return True


def generatePrimes(n):
    
    if n <= 2:
        return []
    
    isPrime = [True] * n
    isPrime[0] = False
    isPrime[1] = False
    
    for i in range (2, math.isqrt(n)):
        if isPrime[i]:
            for x in range (i*i, n, i):
                isPrime[x] = False

    return [i for i in range(n) if isPrime[i]]


def findPrimeFactors(n):

    primes = generatePrimes(math.isqrt(n)+1)
    factors = []

    remaining = n

    for i in primes:
        while remaining % i == 0:
            factors.append(i)
            remaining = remaining / i

    return factors
    


def isPalindrome(n):

    if int(str(n)[::-1]) == n:
        return True
    return False    


