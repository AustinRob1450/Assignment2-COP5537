
import numpy as np
import argparse

def __init__(self, vertices, graph):
    self.V = vertices
    self.graph = {graph}
    print(self.graph)

def Prims():
    return 0

# check degrees: if all even, theres a cycle, else if vertices 2 or more are odd, path
def pathOrCircuit()

def main(FLAGS):
    Prims()

if __name__ == '__main__':
    # Read in the text file here.
    print('---- I tried. ----')
    # Set parameters for Autoencoder
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