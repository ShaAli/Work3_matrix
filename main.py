from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
m2 = new_matrix()
add_edge(matrix,1,2,3,4,5,6)
add_edge(matrix,7,8,9,10,11,12)
add_edge(m2,1,2,3,4,5,6)
add_edge(m2,7,8,9,10,11,12)
print("Original matrix:")
print_matrix(matrix)
print("Testing matrix_mult, multiply matrix by itself:\n")
print_matrix(matrix_mult(matrix,m2))
print("Testing ident():\n")
ident(matrix)
print_matrix(matrix)
print("Testing scalar_mult():\nMultiply matrix by 10:\n")
scalar_mult(matrix,10)
print_matrix(matrix)


draw_lines( matrix, screen, color )
display(screen)
