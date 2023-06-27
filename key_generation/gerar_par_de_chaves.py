from random import randrange
from primePy import primes
from utils.math import modInverse


def gerar_keys(p=23, q=89):
    # PUBLIC
    n = p * q
    t = (p-1)*(q-1) # tocient of p and q
    avaliable_primes = primes.upto(t-1) # primes in the limit [0,t[
    # print(avaliable_primes)
    
    # remove factor primes
    for prime in avaliable_primes:
        if(prime % t == 0):
            avaliable_primes.pop(avaliable_primes.index(prime))
    
    # select a random prime avaliable
    e = avaliable_primes[randrange(0,len(avaliable_primes))]
    public = [e,n]

    # PRIVATE
    d = modInverse(e,t) # find macheable prime
    private = [d,n]
    return [public, private]
    
public, private = gerar_keys()
print(public)
print(private)

