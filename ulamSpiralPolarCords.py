import math
import cairo
import numpy

#Changeable variables
WIDTH, HEIGHT = 1000, 1000
SIZE = 1
NUMBER_OF_PRIMES = 50_000_000

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

#Black background
ctx.set_source_rgba(0.0, 0.0, 0.0, 1) 
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.fill()
ctx.set_source_rgba(0.0, 1.0, 0.0, 1) 

#sieve of eratosthenes
def primes_sieve(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

def primes_sieve_v2(limit):
    limitn = limit + 1
    primes = dict()
    for i in range(2, limitn):
        primes[i] = True

    pf = 2
    while pf ** 2 <= limit:
        if primes[pf]:
            for i in range(pf ** 2, limitn, pf):
                primes[i] = False
        pf += 1

    return primes

def primes_sieve_v3(n):
    flags = numpy.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, n):
        if flags[i]:
            flags[i*i::i] = False
    return numpy.flatnonzero(flags)

def prime_color():
    ctx.set_source_rgba(0.0, 0.0, 1.0, 1) 

def nonPrime_color():
    ctx.set_source_rgba(1.0, 1.0, 0.0, 1) 

def draw_dot(x):
    #radius scaled to how many primes
    radius = (x/maxRad)*WIDTH
    xpos = WIDTH//2 + radius * math.cos(x)
    ypos = HEIGHT//2 - radius * math.sin(x)
    ctx.arc(xpos,ypos,SIZE,0,2*math.pi)
    #ctx.rectangle(xpos, ypos,SIZE,SIZE)
    ctx.fill()

i = 1 #Natural number
j = 0 #Prime counter

primeArray = primes_sieve_v3(NUMBER_OF_PRIMES)

maxRad = primeArray[-1]

print("Primes found")
prime_color()

#loop through all primes found
while(j < len(primeArray)):

    if primeArray[j] == i:
        #prime_color()
        draw_dot(i)
        j += 1
    #else:
    #   nonPrime_color()
    #    draw_dot(i)

    i+= 1

surface.write_to_png("example.png")  # Output to PNG
print("Drawing done")