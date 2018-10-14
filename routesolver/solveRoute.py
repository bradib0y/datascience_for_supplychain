import random # we need random.shuffle, which takes an array and returns that array in a random order
from copy import copy # enables copying an object instead of reference duplication. newObj = copy(someObj)

def distance(place1, place2):
    dx = place2[0]-place1[0]
    dy = place2[1]-place1[1]
    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy    
    return dx + dy

def routeLength(route):
    routeLength = 0
    for i in range(len(route)-1):
        routeLength += distance(route[i], route[i+1])
    return routeLength



def solveRoute(places):
    minimumLength = 9999999
    goodRoute = []
    # try 10K times to create better routes
    for i in range(99999):
        # create a random ordered route with (0,0) at the beginning and the end
        copyOfPlaces = copy(places)
        random.shuffle(copyOfPlaces)
        route = [(0,0)] + copyOfPlaces + [(0,0)]        
        # check if the length of the route is lower than current minimum. If yes, change minimum and save route
        length = routeLength(route)
        if length < minimumLength:
            goodRoute = route
            minimumLength = length
            print("Iteration " + str(i) + ": " + "with length " + str(length) + ", best route so far: " + str(route))

    return goodRoute

