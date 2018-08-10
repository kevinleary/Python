import random
import itertools

def gen_rndtup(n):
    """that creates an infinite sequence of tuples (a, b) where a and b are random integers, 
    with 0 < a,b < n. If n == 7, then a and b could be the numbers on a pair of dice. 
    Use the random module. 
    """


    # for i in range(0, 10):
    
    #     print(str(tup) + " ")
    #tup = ()

    while True:
        a = random.randint(1, n)
        b = random.randint(1, n)
        tup = (a, b)
        yield tup



def main():

    for i in itertools.islice(gen_rndtup(7), 10):
        print(i)
    


main()
