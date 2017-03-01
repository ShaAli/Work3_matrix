import math


def print_matrix( matrix ):
    str = ""
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            str += matrix[r][c]
            str += "\t"
        str += "\n"
    print str

def ident( matrix ):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r==c:
                matrix[r][c] = 1
            else:
                 matrix[r][c] = 0
    return matrix
    

def scalar_mult( matrix, s ):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] = matrix[r][c]*s
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    tmp = new_matrix(len(m2[0], len(m1))
    for r in range(len(m1)):#this is throwing a syntax error!? I'm not sure if I am missing something obvious.
        for c in range(len(m2[0])):
            for i in range(len(m2)):
                     tmp[r][c] += m1[r][i]*m2[i][c]
    return tmp


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
