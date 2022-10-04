"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    count = 0
    i = 3
    while (count < number_of_primes):
        for j in range(2, i):
            if (i % j) == 0:
                break;
            else:
                list.append(i)
                count += 1
                break;
        i += 1
    return list

print(str(primes(1)))
