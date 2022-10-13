# Find Euler Circuit
# Ouput: Text file 

import numpy as np
import argparse

class Fleury:
    def __init__(self, vertices):
        self.V = vertices

    # ---------- addEdge
    # ----------------------------------------

    # Probably to make the graph even.
    def addEdge(self, currentV, nextVertex):
        # Adding each other to each others list so we can cross-verify they are touching.
        self.graph[currentV].append(nextVertex)
        self.graph[nextVertex].append(currentV)
    

    # ---------- removeEdge
    # ----------------------------------------

    # Also means breaking apart the vertices to see where we can remove and still have a good Euler graph
    # Find the vertices pair in the graph, mark it as -1 in their respective lists.
    # ---------- IS THIS PRIMS? ------------
    def removeEdge(self, currentV, pairedV):
        # Uses tuple structure to track what V we are at and what we are iterating towards (the key Vertex to delete)
        for itr, adjacentV in enumerate(self.graph[currentV]):
            if adjacentV == pairedV:
                self.graph[currentV].pop(itr)
        for itr, adjacentV in enumerate(self.graph(pairedV)):
            if adjacentV == currentV:
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


    # ---------- Find the Start
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
    

    # ---------- Print Graph
    # ----------------------------------------

    def printEuler(self, currentV):
        for itr in self.graph[currentV]:
            if self.checkEdge(currentV, itr):
                print(currentV, itr)
                self.removeEdge(currentV, itr)
                self.printEuler(itr)

            
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
        firstCount = self.depthFirstSearch(currentV, visited)
        self.removeEdge(currentV, pairedV)
        secondCount = self.depthFirstSearch(currentV, visited)
        self.addEdge(currentV, pairedV)
        
        return firstCount > secondCount
    
    # ---------- Euler Main
    # ----------------------------------------
    def Euler(self):
        currentV=0
        for itr in range(self.V):
            if len(self.graph[itr]) % 2 != 0:
                currentV=itr
                break
        print("\n")
        self.printEuler(currentV)
            


def main(FLAGS):
    # with open('Data.txt', 'r') as f:
    #     data = f.readlines()
    data = np.loadtxt(FLAGS.file, dtype=str)
    print('data:\n', type(data))
    print(np.shape(data))
    print(len(data))

    # ---------- Method Calls
    # ----------------------------------------

    graph = Fleury(data)


    output = Fleury.printEuler()
    outputFile = open("output.txt", "w")
    outputFile.write(output)

    
if __name__ == '__main__':
    # Read in the text file here.
    print('---- I tried. ----')
    # Set parameters for Sparse Autoencoder
    parser = argparse.ArgumentParser('Assignment 2.')
    parser.add_argument('--file',
                        type=str, default='./Data.txt',
                        help='Please enter your file as a command line argument ex.("Data.txt").')
    parser.add_argument('--start_vertex',
                        type=str, default='08',
                        help='Please enter your file as a command line argument.')
                        
                        
    FLAGS = None
    FLAGS, unparsed = parser.parse_known_args()
    
    main(FLAGS)