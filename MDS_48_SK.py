from AES import *
from CONTROL import *
from CNF import *
from TK1 import *
import os

if __name__ == '__main__':
    P = P_48_MDS_TK1

    V = MC_48_MDS

    #TKP = [ 28, 0, 18, 21, 12, 30, 11, 23, 9, 8, 5, 15, 7, 27, 13, 20, 26, 6, 29, 14, 3, 24, 10, 22, 1, 2, 19, 31, 16, 17, 25, 4 ]
    
    AES = AES_DIFF_BOUND_SK( 4, 8, P, V  )

    Control = Control(AES, '.AES_48_MDS_SK_10_' )

    Control.flow( 20 )
