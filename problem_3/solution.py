## Method
import math

even_test = 100
test_case = 13195
problem = 600851475143

def sqrt(num):
    # returns the square root of a number to the nearest integer
    return int(math.sqrt(num))

def sieve(num): # nod to Sieve of Eratosthenes
    # finds the largest prime factor of a given number by iteratively factoring out increasingly large primes
    # the result of each new division is saved in remainder
    # we know that all factors removed are prime because smaller primes are factored out first
    remainder = num
    while remainder % 2 == 0: 
        remainder = remainder//2 # this while loop removes all multiples of 2 from the given number
    divisor = 3
    while divisor <= sqrt(remainder): # this while loop removes all multiples of odd numbers up to the square root of the previous remainder
        while remainder % divisor == 0: 
            remainder = remainder//divisor 
        divisor += 2 # increments to the next odd number
    if remainder > 1:
        return remainder # if remainder doesn't reach 1, the largest prime is greater than the square root of the previous remainder
    # since its factor pair has to be smaller and therefore already removed, the last remainder is returned as the largest prime
    return divisor-2 # reverses the last time divisor was incremented so that the divisor to produce the remainder of 1 is returned as the largest prime

## Validation
import sympy # library for symbolic maths 
from sympy import primefactors

def validation(num, ans):
    # verifies answer against the sympy function for prime factors
    largest_prime = primefactors(num)[-1] # primefactors() provides the prime factors as a list in ascending order
    if largest_prime == ans:
        return True
    else:
        return False

def result(num):
    # wrapper
    print(f'{sieve(num)} is the largest prime factor of {num}')
    return validation(num, sieve(num))

print(result(even_test))
print(result(test_case))
print(result(problem))
