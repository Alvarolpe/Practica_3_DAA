# Función test de arbol expandido minimo

import numpy as np
from algoritmos import prim, kruskal
from practica_3 import to_adjacency_matrix

def test():
    V1 = {0,1,2,3}
    E1 = {(0, 2, 9), (3, 2, 2), (0, 3, 6), (1, 2, 4), (0, 1, 5), (1, 3, 3)}
    M1 = to_adjacency_matrix(V1,E1)
    MST1_gold = {(3, 2, 2), (0, 1, 5), (1, 3, 3)}
    MST1_prim = prim(M1)
    MST1_kruskal = kruskal(V1,E1)

    V2 = {0,1,2,3,4}
    E2 = {(3, 4, 6), (1, 2, 1), (0, 2, 9), (1, 4, 7), (0, 3, 4), (3, 1, 2), (2, 3, 3), (2, 4, 9), (0, 4, 8), (0, 1, 5)}
    M2 = to_adjacency_matrix(V2,E2)
    MST2_gold = {(3, 4, 6), (1, 2, 1), (0, 3, 4), (3, 1, 2)}
    MST2_prim = prim(M2)
    MST2_kruskal = kruskal(V2,E2)

    assert MST1_gold == MST1_prim 
    assert MST1_gold == MST1_kruskal
    assert MST2_gold == MST2_prim
    assert MST2_gold == MST2_kruskal

def main():
    test()
    
if __name__ == "__main__":
    main()