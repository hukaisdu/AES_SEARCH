from CNF import *
from AES import *

class AES_DIFF_BOUND_SK( CNF, AES ):  
    def __init__(self, number_of_row, number_of_column, P, V, TKP = None ):
        CNF.__init__(self)
        AES.__init__( self, number_of_row, number_of_column, P, TKP )
        self._mcV = V

    def mix_column( self, X, Y ):  
        # first column
        for c in range( self._C ):
            Xc = []
            Yc = []
            for r in range(self._R ):
                Xc.append( X[ r * self._C + c ] ) 
                Yc.append( Y[ r * self._C + c ] )

            #self.gen_constr_exclude_vetcor( Xc + Yc, self._mcV )
            self.gen_constr_exclude_vector( Xc + Yc, self._mcV )

    def gen_diff_model( self, R, obj, value_bound ):
        self.reset()

        # generate variables
        X = [ [ self.gen_var() for i in range(self._N) ] for j in range(R + 1) ]

        # ShiftRows
        for r in range( R ):
            tmp = self.perm( X[r] ) 
            self.mix_column( tmp, X[r + 1] )

        self.gen_constr_exclude_vector( X[0], [ ['0'] * self._N ] ) 

        round_variable = []

        Obj = []
        for r in range( R ):
            Obj += X[r] 

            if R >= 2 and r < R - 1: 
                round_variable.append( len( Obj ) - 1  )

            #print( Obj )

        #print( R, round_variable, value_bound )
        self.seq_sum( Obj , obj, round_variable, value_bound )
