from AES import *
from CONTROL import *
from CNF import *
from SK import *
import os

if __name__ == '__main__':
    P = P_44_ALMOST
    V = MC_44_ALMOST_PRECISE
    AES = AES_DIFF_BOUND_SK( 4, 4, P, V )
    Control = Control(AES, '.AES_44_ALMOST_PRECISE_' )
    Control.flow( 20 )
