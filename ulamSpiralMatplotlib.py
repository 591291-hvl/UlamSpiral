from copy import deepcopy
import math
import time

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation


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


N = 100
orientation = 0

totalDistanceToWrite = 0
distanceWritten = 0
lineIncrement = False

i = 1
j = 0
grid = np.zeros((N,N), np.int32).tolist()

#N = 5
#Midpoint of table is [N/2][N/2]
#[2][2]
#0, 0, 0, 0, 0
#0, 0, 0, 0, 0
#0, 0, X, 0, 0
#0, 0, 0, 0, 0
#0, 0, 0, 0, 0
x = N//2
y = N//2

grid[x][y] = 1
primeArray = primeList(N*N)


def run(data):
    global i
    global j
    global grid
    global N

    global orientation
    global totalDistanceToWrite
    global distanceWritten
    global lineIncrement

    global x
    global y

    if primeArray[j] == i:
        grid[x][y] = 1
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

    
    mat.set_data(grid)
    return [mat]




fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, run, interval=.01, save_count=2)
plt.show()
