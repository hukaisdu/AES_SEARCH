from AES import *
from SK import *

class AES_DIFF_BOUND_TK1_HALF( AES_DIFF_BOUND_SK ):
    def __init__(self, number_of_row, number_of_column, P, MC_V, TKP ):
        AES_DIFF_BOUND_SK.__init__( self, number_of_row, number_of_column, P, MC_V, TKP )

    def gen_diff_model( self, R, obj, value_bound ):
        self.reset()

        X = [ [ self.gen_var() for i in range( self._N ) ] for j in range( R + 1 ) ]
        Y = [ [ self.gen_var() for i in range( self._N ) ] for j in range( R ) ]
        K = [ self.gen_var() for i in range( self._N ) ]

        # set k constraints
        '''
        for i in range(16):
            if i in [2, 8, 9, 13]:
                s = '%d 0' % K[i]
            else:
                s = '-%d 0' % K[i]
            self.addClause( s )
        # set the first constraints:
        for i in range(16):
            if i in [9]:
                s = '%d 0' % X[0][i]
            else:
                s = '-%d 0' % X[0][i]
            self.addClause( s )
        '''

        for r in range( R ):
            # encryption
            self.HALFXOR( X[r], K, Y[r] ) 
            Y[r] = self.perm( Y[r] )
            self.mix_column( Y[r], X[r + 1] )

            # key schedule
            K = self.TK_perm( K )

            #print( K )

        self.gen_constr_exclude_vector( K, [ ['0'] * self._N ] ) 

        round_variable = []

        Obj = []
        for r in range( R ):
            Obj += X[r] 

            if R >= 2 and r < R - 1: 
                round_variable.append( len( Obj ) - 1  )

            #print( Obj )

        #print( R, round_variable, value_bound )
        self.seq_sum( Obj, obj, round_variable, value_bound )















    





