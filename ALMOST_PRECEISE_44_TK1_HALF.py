from AES import *
from CONTROL import *
from CNF import *
from TK1HALF import *
from SK import *
import os

if __name__ == '__main__':
    P = P_44_ALMOST
    V = MC_44_ALMOST_PRECISE
    TKP = [ 10,13,12,9,15,8,11,14,0,1,2,3,4,5,6,7 ]
    AES = AES_DIFF_BOUND_TK1_HALF( 4, 4, P, V, TKP  )
    Control = Control(AES, '.AES_44_ALMOST_PRECISE_TK1_HALF_' )
    Control.flow( 20 )
