from AES import *
from CONTROL import *
from CNF import *
from TK1 import *
from SK import *
import os

if __name__ == '__main__':
    P = P_48_MDS_TK1

    V = MC_48_MDS

    TKP = [ 28, 0, 18, 21, 12, 30, 11, 23, 9, 8, 5, 15, 7, 27, 13, 20, 26, 6, 29, 14, 3, 24, 10, 22, 1, 2, 19, 31, 16, 17, 25, 4 ]
    
    AES = AES_DIFF_BOUND_TK1( 4, 8, P, V, TKP  )

    Control = Control(AES, '.AES_48_MDS_TK1_5' )

    value = Control.AttackRound( 11, [0, 1, 4, 8, 17, 28, 38, 46, 51, 60] )
    #value = Control.AttackRound( 5, [0, 1, 4, 8 ] )

    print( value )
