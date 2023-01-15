from AES import *
from SK import *
from TK1 import *
import os
from const import *

class Control:
    def __init__( self, AES, name ):
        self._AES = AES
        self._file_index = 0
        self._name = name

    def getFileName( self ):
        return self._name + str( self._file_index ) + '.cnf' 

    def parse_result( self, res ):
        with open( res, 'r' ) as f:
            lines = f.readlines()
            for line in lines:
                #if 's UNSATISFIABLE' in line:
                if 'UNSATISFIABLE' in line:
                    return False
                #if 's SATISFIABLE' in line:
                elif 'SATISFIABLE' in line:
                    return True
            else:
                print( "Error" )
                exit(0)

    def AttackRound( self, R, value_bound ):
        # current bound 
        bound = 0
        # generate a name

        #round_bound = {}

        #round_bound [ 0 ] = 0

        bound = value_bound[ -1 ]

        for increase in range( 1000 ):
            self._AES.gen_diff_model( R, bound + increase,  value_bound )

            cnf_name = self.getFileName()

            self._AES.printCNF( cnf_name )

            os.system( 'cadical -n -q %s > %s.res' % ( cnf_name, cnf_name ) )

            parse_res = self.parse_result( cnf_name + '.res' ) 

            #print( r, bound, parse_res )

            if self.parse_result( cnf_name + '.res' ) == True:
                return bound + increase
                break
            else:
                continue

        #value_bound.append( round_bound [ r ]  )

        #print( 'Round: ', r,  'Bound: ', round_bound[r], flush = False )

        return -1

    def flow( self, R ):
        # current bound 
        bound = 0
        # generate a name

        round_bound = {}

        round_bound [ 0 ] = 0

        value_bound = []
        
        for r in range(1, R + 1):
            bound = round_bound[ r - 1 ]
            for increase in range( 1000 ):
                self._AES.gen_diff_model( r, bound + increase,  value_bound )

                cnf_name = self.getFileName()

                self._AES.printCNF( cnf_name )

                os.system( 'cadical -n -q %s > %s.res' % ( cnf_name, cnf_name ) )

                parse_res = self.parse_result( cnf_name + '.res' ) 

                #print( r, bound, parse_res )

                if self.parse_result( cnf_name + '.res' ) == True:
                    round_bound [ r ] = bound + increase
                    break
                else:
                    continue

            value_bound.append( round_bound [ r ]  )

            print( 'Round: ', r,  'Bound: ', round_bound[r], flush = False )

        return round_bound

if __name__ == '__main__':
    P = P_44_ALMOST
    V = MC_44_ALMOST_PRECISE
    AES = AES_DIFF_BOUND_SK( 4, 4, P, V )
    Control = Control(AES, '.AES_44_ALMOST_PRECISE_' )
    Results = Control.flow( 20 )

    print( Results )


    




