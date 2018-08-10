import sys
import math

class PrimeSeq:

    __primes = list()       #instance attribute???

    def __init__(self, count):
        """ Default initalizer 

        """
        self.count = count
        

    def __iter__(self):
        """ needs to have __iter__() to be for() compatable

        """
        
        return self

    def __next__(self):
        """ Aslo needs __next__() to be for compatable
        
        """
        #if len(self.__primes) <= self.count:
        """ if self.n <= self.count:
            for p in range(2, sys.maxsize**10):
                for i in range(2, p):
                    if p % i == 0:
                        break
                    else:
                        
                        self.n +=1 
                        return self.__primes.append(p) """

        if self.count > 2:
            for n in range(2, self.count):
                if self.__isprime(n):
                    n += 1
                    return n
        else:
            raise StopIteration

    def __isprime(self, n):
        """ Checks if the number is prime 
            returns boolean
        """
        self.n = n

        for i in range(2, self.n):
            if self.n % i == 0:
                return False
        return True

#2B
def prime_gen(n):
    """takes an integer n >= 0 and produces the sequence of the first n prime numbers. 
    This generator is defined as a function that uses the yield keyword to output a value

    """
    start = 2
    for i in range(start, int(math.sqrt(n)) + 1):
        if n % 1 == 0:
            break
        else:
            yield i
    


#2A

# primeseq = PrimeSeq(100)
# for p in primeseq:
#     print(p)

#2B
for p in prime_gen(10):
    print(p)