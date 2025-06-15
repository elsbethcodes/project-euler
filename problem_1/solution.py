## Problem: sum the multiples of 3 or 5 below 1000.

## Test Case:
# The sum of multiples of 3 or 5 below 10 is 23.

## Insight: 
# The multiples of 3 and the multiples of 5 form arithmetic sequences.

## Method: 
# Find the summations of these sequences up to their largest term below 1000 and subtract the intersection of their terms.

## Formulae:
# Define a : first term, d : common difference and n : number of terms.
# Then the last term of an arithmetic sequence, l = a + (n-1)d.
# The summation of an arithmetic sequence, Sn = (a+l)/2 * n. 
# Or in words, Sn is the average of the first term and last term multiplied by the number of terms.

## Method:
def first_term(d):
  return d # In this case a=d

def number_of_terms(d,X):
  # if X is a multiple of d then decrease the number of terms by 1 to exclude X
  if X%d == 0: 
    return int(X/d) - 1
  # otherwise round down to the nearest integer when d divides X
  else:
    return int(X/d) 

def last_term(d,X):
  return first_term(d) + (number_of_terms(d,X) - 1) * d

def summation(d,X):
  return ((first_term(d) + last_term(d,X))/2 * number_of_terms(d,X))

## Test Case:
summation_to_10 = summation(3,10) + summation(5,10) - summation(15,10)
print(int(summation_to_10))

## Solution:
summation_to_1000 = summation(3,1000) + summation(5,1000) - summation(15,1000)
print(int(summation_to_1000))
