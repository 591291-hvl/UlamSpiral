import math
import cairo

WIDTH, HEIGHT = 1000, 1000

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
    ctx.set_source_rgba(0.0, 1.0, 0.0, 1) 
    xpos = WIDTH//2 + x * math.cos(x)
    ypos = HEIGHT//2 - x * math.sin(x)
    ctx.rectangle(xpos, ypos,2,2)
    ctx.fill()

def draw_nonPrime(x):
    ctx.set_source_rgba(1.0, 0.0, 0.0, 1) 
    xpos = WIDTH//2 + x * math.cos(x)
    ypos = HEIGHT//2 - x * math.sin(x)
    ctx.rectangle(xpos, ypos,2,2)
    ctx.fill()


i = 1
j = 0

x = WIDTH//2
y = HEIGHT//2

primeArray = primes_sieve(WIDTH*WIDTH)

print("Primes found")

while(j < len(primeArray)):

    if primeArray[j] == i:
        draw_prime(i)
        j += 1
    else:
        draw_nonPrime(i)
    

    i+= 1

surface.write_to_png("example.png")  # Output to PNG
print("Drawing done")