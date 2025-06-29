## Problem: By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

## Test Case:
# None given.

## Insight:
# By observing the Fibonacci sequence from 1, 1, 2, 3, 5, 8, 13, ... we see that every third term is even.
# This pattern must hold since each term is the sum of the previous two terms: Fn = Fn-1 + Fn-2 so the pattern of even numbers is periodic (with period 3).

## Method: 
# Find the sequence that represents the even Fibonacci numbers.
# Approximate how many terms of that sequence are below 4 million by using Binet's formula for the nth term of a Fibonacci sequence.
# Perform the summation.

## Formulae:
# Binet's Formula for the nth term of a Fibonacci sequence is (φ^n + (1-φ)^n)/√5.
# Since φ is approximately 1.6, |1-φ| < 1, therefore as n tends to infinity, (1-φ)^n tends to infinity.
# Therefore Binet's formula approximates the nth term of the Fibonnaci sequence as φ^n/√5.
# This means that our sequence for the even Fibonacci numbers becomes 1/√5 * (φ^3, φ^6, φ^9, ... )
# This is a geometric sequence with first term, a = φ^3/√5 and common ratio, r = φ^3 so we will also use that the summation of a geometric sequence up to term n is Sn = a(1-r^n)/(1-r).
# We will also need the definition of a log to find the index of the Fibonacci term closest to 4 million.
# Definition of a log: a ^ n = b is equivalent to n = log a(b).

## Method:
import math
phi = (1 + math.sqrt(5))/2

def num_terms_fib():
  # Returns the number of terms, n, for which the even numbers of the Fibonnaci sequence are below 4 million.
  # Assume that 4 million is a Fibonnaci number.
  # 4,000,000 = φ^n/√5 where n is the index of 4,000,000 in the Fibonnaci sequence.
  # Using the definition of a logarithm, log φ(4,000,000*√5) = n.
  n = math.log(4000000*math.sqrt(5), phi)
  return int(n) # Rounds down n to the nearest integer.

def num_terms_even_fib():
    return int(num_terms_fib()/3) 

print(f'There are {num_terms_even_fib()} even Fibonnaci numbers below 4m.')

def summation(a,r,n):
  # Returns the output of the summation formula
  return (a*(1-r**n)/(1-r))

## Test Case:
# Pass

## Solution:
solution = summation(a = (phi**3)/math.sqrt(5), r = phi**3, n = num_terms_even_fib())
print(f'They sum to {int(round(solution,0))}.')
