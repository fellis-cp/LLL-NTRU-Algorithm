from LLL import *
import timeit

start = timeit.default_timer()
#inputan
mat = [[1, 0, 0, 0, 0, 1, 20, 0, 0, 20],[0, 1, 0, 0, 0, 20, 1, 20, 0, 0],[0, 0, 1, 0, 0, 0, 20, 1, 20, 0],[0, 0, 0, 1, 0, 0, 0, 20, 1, 20],[0, 0, 0, 0, 1, 20, 0, 0, 20, 1],[0, 0, 0, 0, 0, 41, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 41, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 41, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 41, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 41]]
print("contoh : ")
mat1 = create_matrix(mat)
print("mat1 : ")
print_mat(mat1)
print("mat1 is lll?", islll(mat1))

print("reduce mat : ")
mat1pass = lll_reduction(mat1)
print_mat(mat1pass)
print("mat1 is lll?", islll(mat1pass))

stop = timeit.default_timer()
print("time : ",stop - start)
