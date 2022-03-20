import math
import cairo

WIDTH, HEIGHT = 1000, 1000
SIZE = 1
NUMBER_OF_PRIMES = 2_00_000

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

def prime_color():
    ctx.set_source_rgba(0.0, 0.0, 1.0, 1) 

def nonPrime_color():
    ctx.set_source_rgba(1.0, 1.0, 0.0, 1) 

def draw_dot(x):
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
        prime_color()
        draw_dot(i)
        j += 1
    #else:
    #   nonPrime_color()
        draw_dot(i)
    
    
    i+= 1

surface.write_to_png("example.png")  # Output to PNG
print("Drawing done")