import math


def print_matrix( matrix ):
    ret = ""
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            ret += str(matrix[r][c])
            ret += "\t"
        ret += "\n"
    print ret

def ident( matrix ):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r==c:
                matrix[r][c] = 1
            else:
                 matrix[r][c] = 0
    

def scalar_mult( matrix, s ):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] = matrix[r][c]*s
    return matrix

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    if(len(m1[0]) == len(m2)):
        tmp = new_matrix(len(m2[0]), len(m1))
        for r in range( len(m2[0])):
            for c in range(len(m2)):
                num = 0;
                for i in range(len( m1[c])):
                    num += m1[c][i] * m2[i][r];
                tmp[c][r] = num
        for r in range(len(m2)):
            for c in range(len(m1[r])):
                m2[r][c] = tmp[r][c]
        return tmp
    else:
        print "Cannot multiply these matrices"


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
