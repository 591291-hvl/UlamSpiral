import math
import cairo

WIDTH, HEIGHT = 3840, 2160

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, WIDTH)
ctx = cairo.Context(surface)

ctx.set_source_rgba(0.0, 0.0, 0.0, 1) 
ctx.rectangle(0, 0, WIDTH, WIDTH)
ctx.fill()
ctx.set_source_rgba(0.0, 1.0, 1.0, 1) 


def findPrime(n):
    numberOfDividable = 0
    for i in range(1,1+int(math.sqrt(n))):
        #print(i)
        if n % i == 0:
            numberOfDividable += 1
        if numberOfDividable >= 2:
            return False
    return True

def primeList(x):

    array = []
    array.append(2)

    for i in range(2,x):
        addToArray = True
        for j in array:
            if i%j == 0:
                addToArray = False
                break
        if addToArray:
            array.append(i)
    return array


#N = 1000
orientation = 1

totalDistanceToWrite = 0
distanceWritten = 0
lineIncrement = False

i = 1
j = 0

x = WIDTH//2
y = HEIGHT//2

primeArray = primeList(WIDTH*HEIGHT)


while(j < len(primeArray)):

    if primeArray[j] == i:
        #draw
        #ctx.arc(x,y,1,0,2*math.pi)
        ctx.rectangle(x,y,1,1)
        ctx.fill()
        j += 1

    i+= 1
    
    #based on orientation move in that direction
    #4 if-checks?
    if orientation == 0:
        x += 1
    elif orientation == 1:
        y += 1
    elif orientation == 2:
        x -= 1
    elif orientation == 3:
        y -= 1


    #Every other, change orientation
    if totalDistanceToWrite == distanceWritten:
        distanceWritten = 0
        if lineIncrement:
            totalDistanceToWrite += 1
            lineIncrement = False
        else:
            lineIncrement = True
        orientation = (orientation+1)%4
    else:
        distanceWritten += 1



surface.write_to_png("example.png")  # Output to PNG
print("done")