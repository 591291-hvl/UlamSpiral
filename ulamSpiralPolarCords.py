import math
import cairo

WIDTH, HEIGHT = 2000, 2000
SIZE = 2
NUMBER_OF_PRIMES = 1_00_000

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgba(0.0, 0.0, 0.0, 1) 
ctx.rectangle(0, 0, WIDTH, HEIGHT)
ctx.fill()
ctx.set_source_rgba(0.0, 1.0, 0.0, 1) 

def primes_sieve(limit):
    limitn = limit+1
    primes = dict()
    for i in range(2, limitn): primes[i] = True

    for i in primes:
        factors = range(i,limitn, i)
        for f in factors[1:]:
            primes[f] = False
    return [i for i in primes if primes[i]==True]

def draw_prime(x):
    ctx.set_source_rgba(0.0, 0.0, 1.0, 1) 
    radius = (x/primeArray[-1])*WIDTH
    xpos = WIDTH//2 + radius * math.cos(x)
    ypos = HEIGHT//2 - radius * math.sin(x)
    ctx.arc(xpos,ypos,SIZE,0,2*math.pi)
    #ctx.rectangle(xpos, ypos,SIZE,SIZE)
    ctx.fill()

def draw_nonPrime(x):
    ctx.set_source_rgba(1.0, 1.0, 0.0, 1) 
    radius = (x/primeArray[-1])*WIDTH
    xpos = WIDTH//2 + radius * math.cos(x)
    ypos = HEIGHT//2 - radius * math.sin(x)
    ctx.arc(xpos,ypos,SIZE,0,2*math.pi)
    #ctx.rectangle(xpos, ypos,SIZE,SIZE)
    ctx.fill()


i = 1
j = 0

x = WIDTH//2
y = HEIGHT//2

primeArray = primes_sieve(NUMBER_OF_PRIMES)

print("Primes found")

while(j < len(primeArray)):

    if primeArray[j] == i:
        draw_prime(i)
        j += 1
    #else:
    #   draw_nonPrime(i)
    

    i+= 1

surface.write_to_png("example.png")  # Output to PNG
print("Drawing done")