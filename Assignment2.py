# Find Euler Circuit
# Ouput: Text file
# 
# Austin Roberts
# Fall 2022
# COP5537

import numpy as np
import argparse

class Fleury:
    def __init__(self, input):
        self.graph = input
        self.V = len(input)
 

    def countOdds(self):
        matrix=[]
        size=self.V

        for itr in range(size):
            matrix.append(sum(self.graph[itr]))

        for itr in range(size-1, -1, -1):
            if ((matrix[itr] % 2) == 1):
                odd+=1
    
        if odd > 2:
            print("No solution")
            return 0
        return odd

    def fluery(self, start):
        print(self.graph)
        size = self.V
        odd=0
        matrix = []
        visited = [False]*self.V
        # start = int(FLAGS.start_vertex)
        circuit = []
            
        odds = countOdds(self)

        current = start
        while sum(self.graph[current]) != 0  or (circuit != []):
            
            print("Im in")
            
            if sum(self.graph[current]) == 0:
                print("here")
                circuit.append(current+1)
                current = circuit.pop(-1)
            else:
                for itr in range(size):
                    # EDGE FOUND BOYS
                    print("self.graph[current][itr]", self.graph[current][itr])
                    if self.graph[current][itr] == 1:
                        circuit.append(current)
                        # Elimainate edge since we've been here
                        self.graph[current][itr] = 0
                        self.graph[itr][current] = 0
                        current = itr
                        break
        for itr in circuit:
            print(itr, '-', end=' ')
        print(current+1)
        


def main(FLAGS):
    # input = np.loadtxt(FLAGS.file, dtype=str)
    # print('data:\n', type(input[0]))


    input=[
        [0, 1, 0, 0, 1], 
         [1, 0, 1, 1, 1], 
         [0, 1, 0, 1, 0], 
         [0, 1, 1, 0, 1], 
         [1, 1, 0, 1, 0]]

    print(np.shape(input))
    print(len(input))
	

    # ---------- Method Calls
    # ----------------------------------------
    graph = Fleury(input)
    graph.fluery(1)






if __name__ == '__main__':
    # Read in the text file here.
    print('---- I really tried. ----')
    # Set parameters for Sparse Autoencoder
    parser = argparse.ArgumentParser('Assignment 2.')
    parser.add_argument('--file',
                        type=str, default='./Data.txt',
                        help='Please enter your file as a command line argument ex.("Data.txt").')
    parser.add_argument('--start_vertex',
                        type=str, default='1',
                        help='Please enter your file as a command line argument.')
                        
                        
    FLAGS = None
    FLAGS, unparsed = parser.parse_known_args()
    
    main(FLAGS)