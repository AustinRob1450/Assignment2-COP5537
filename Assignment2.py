import enum
from re import T
from tracemalloc import start
import pandas
import sys
import numpy as np
import json

class Fleury():
    def __init__(self, vertices, graph):
        self.V = vertices
        self.graph = {graph}
        print(self.graph)

    # ---------- addEdge
    # ----------------------------------------

    # Probably to make the graph even.
    def addEdge(self, currentV, newVertex):
        # Adding each other to each others list so we can cross-verify they are touching.
        self.graph[currentV].append(newVertex)
        self.graph[newVertex].append(currentV)
    

    # ---------- removeEdge
    # ----------------------------------------

    # Also means breaking apart the vertices to see where we can remove and still have a good Euler graph
    # Find the vertices pair in the graph, mark it as -1 in their respective lists.
    # ---------- IS THIS PRIMS? ------------
    def removeEdge(self, currV, pairedV):
        # Uses tuple structure to tack what V we are at and what we are iterating towards (the key Vertex to delete)
        for itr, adjacentV in enumerate(self.graph[currV]):
            if adjacentV == pairedV:
                self.graph[currV].pop(itr)
        for itr, adjacentV in enumerate(self.graph(pairedV)):
            if adjacentV == currV:
                self.graph[pairedV].pop(itr)
    

    # ---------- isBridge
    # ----------------------------------------
    
    # Is adjacnecy measured in connections to a vertex?
    ## DOUBLE CHECK
    def isBridge(self, currentV):
        degree = 0
        for itr in enumerate(self.graph[currentV]):
            degree += 1
            if (degree > 1):
                return False
        return True


    # ---------- findStart
    # ----------------------------------------

    # If there are no odd degree vertices we can pick any V as the start.
    # If there is an odd degree vertices we have to pick it.
    def findStart(self):
        degree = 0
        for itr in enumerate(self.graph):

            for atr in enumerate(self.graph):
                degree += 1

            if degree % 2 != 0:
                return itr
        return 0
    

    # ---------- depthFirstSearch
    # ----------------------------------------

    # We need a list of visted vertices in order to perform DFS
    def depthFirstSearch(self, currentV, visited):
        visited[currentV] = True
        count=1
        for itr in self.graph[currentV]:
            if visited[itr] == False:
                count += count + self.depthFirstSearch(itr, visited)
        return count


    # ---------- checkEdge
    # ----------------------------------------

    # True in Two conditions: 
    # 1.) One one adj vertex of currentV. 
    # 2.) Not a bridge, etc.
    def checkEdge(self, currentV, pairedV):
        visited= False * self.V
        # Only 1 other vertex adjacent
        if len(self.graph[currentV] == 1):
            return True
        counter = self.depthFirstSearch(currentV, visited)
        self.removeEdge(currentV, pairedV)
        
def main():
    # with open('Data.txt', 'r') as f:
    #     data = f.readlines()
    data = np.loadtxt('Data.txt', dtype=str)
    print('data:\n', type(data))
    # print('data:\n', data)

    # graph = [[1,2,3,4,],
    #          [5,6,7,8,]]
    for x in data:
        for y in x:
            break
    print(np.shape(data))
    print(data[20][0])

    
if __name__ == '__main__':
    # Read in the text file here.
    print('---- I tried. ----')
    main()