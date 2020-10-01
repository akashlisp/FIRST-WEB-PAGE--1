import PRIME
from collections import Counter


def factors(number):
    primes = PRIME.Prime(number).primes()
    if number==1:
        return "1-->1"
    if PRIME.is_prime(number):
        return f"""1-->1
        {number}-->1"""
    else:
        result = []
        while number != 1:
            for i in primes:
                if number % i == 0:
                    number /= i
                    result.append(i)
                    break
    count = Counter(result)
    for i,j in count.items():
        print(f'{i}-->{j}')
    return ''


def hcf(x, y):
    while y:
        x, y = y, x % y
    return x


print(factors(258225617))
