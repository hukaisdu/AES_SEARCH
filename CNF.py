
class CNF: 
    def __init__( self ):
        self._V = 0
        self._clause = []

    def reset( self ):
        self._V = 0
        self._clause = []

    def addClause( self, c ):
        self._clause.append( c )

    def seq_sum( self, X, k, round_bound, value_bound ):
        if k > 0:
            n = len( X )
            #S = [ [ self._V + ( k * j + i ) for i in range( k ) ] for j in range( n - 1 ) ]
            S = [ [ self.gen_var() for i in range( k ) ] for j in range( n - 1 ) ]

            self._V += k * ( n - 1 )

            s = '-%d %d 0' % ( X[0], S[0][0] )
            #Clause.append ( s )
            self.addClause( s )

            for j in range(1, k):
                s = '-%d 0' % ( S[0][j] )
                self.addClause( s )

            for i in range( 1, n - 1 ):
                s = '-%d %d 0' % ( X[i], S[i][0] )
                self.addClause( s )
                s = '-%d %d 0' % ( S[i - 1][0], S[i][0] )
                self.addClause( s )

                for j in range(1, k):
                    s = '-%d -%d %d 0' % ( X[i], S[i - 1][j - 1], S[i][j] )
                    self.addClause( s )
                    s = '-%d %d 0' % ( S[i - 1][j], S[i][j] )
                    self.addClause( s )

                s = '-%d -%d 0' % ( X[i], S[i- 1][k - 1] )
                self.addClause( s )

            s = '-%d -%d 0' % ( X[n - 1], S[n - 2][k - 1] )
            #Clause.append ( s )
            self.addClause( s )

            #print( round_bound, value_bound )

            #print( X )

            if len(round_bound ) >= 1:
                for rr in range( len( round_bound ) ):
                    var = round_bound [ rr ]
                    for i in range(1, var + 1):
                        #print( rr, value_bound[rr] )
                        #print( i, X[i] )
                        #input()
                        s = '-%d -%d 0' % ( X[i],  S[i-1][ ( k - value_bound[::-1][rr] ) - 1 ] )
                        self.addClause( s )
                    #input()

        else:
            for x in X:
                s =  '-%d 0' % x
                self.addClause( s )

    def gen_var( self ):
        self._V += 1
        return self._V 

    def gen_constr_exclude_vector( self, X, V ):
        L = len( X )
        for v in V:
            s = ''
            for i in range(L):
                if v[i] == '1':
                    s += '-%d ' % ( X[i] ) 
                elif v[i] == '0':
                    s += '%d ' % ( X[i] ) 
                else:
                    pass

            s += '0' 

            self.addClause( s )

    def printCNF( self, filename ):
        with open( filename, 'w' ) as f:
            f.write( 'p cnf %d %d \n' % ( self._V, len( self._clause ) ) ) 
            for clause in self._clause:
                f.write( '%s \n' % clause ) 

if __name__ == '__main__':
    V = [ [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0,0,0], [0,1,1], [1,0,1], [1,1,0] ]

    CNF = CNF()

    X = [ CNF.gen_var() for i in range(3) ]

    CNF.gen_constr_exclude_vector( X, V ) 

    CNF.printCNF( 'test.cnf' ) 



