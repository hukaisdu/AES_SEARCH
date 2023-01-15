from AES import *
from CONTROL import *
from CNF import *
from TK1 import *
from SK import *
import os

if __name__ == '__main__':
    P = P_44_ALMOST
    V = MC_44_ALMOST_PRECISE
    TKP = [ 12, 10, 11, 7, 1, 14, 13, 15, 9, 4, 5, 6, 3, 8, 0, 2 ]
    AES = AES_DIFF_BOUND_TK1( 4, 4, P, V, TKP  )
    Control = Control(AES, '.AES_44_ALMOST_PRECISE_TK1_' )
    Control.flow( 20 )
