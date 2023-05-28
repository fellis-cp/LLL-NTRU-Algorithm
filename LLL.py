from fractions import Fraction
import math
import random
import numpy as np
from random import randint
import base64
import binascii
from scipy import linalg

#matrix multiplication
def mat_mult(a,b):
    m = len(a)
    n = len(b[0])
    p = len(a[0])
    res = [[0 for j in range(n)]for i in range(m)]
    for i in range(m):
        for j in range(n):
            coeff = 0
            for k in range(p):
                coeff += a[i][k] * b[k][j]
            res[i][j] = coeff
    return res

#scalar product
def scalar_product(a,b):
    m = len(a)
    res = Fraction(0)
    for i in range(m):
        res += a[i] * b[i]
    return res

#display  matrix
def print_mat(n):
    maxlen = 0
    for row in n:
        for f in row:
            if len(str(f)) > maxlen:
                maxlen = len(str(f))
    for row in n:
        row_str = ""
        for f in row:
            difflen = maxlen - len(str(f))
            sep = " "
            for i in range(difflen):
                sep = sep + " "
            row_str = row_str + sep + str(f)
        print(row_str)

#display vector
def print_vector(v):
    row_str = " ".join("%s" % i for i in v)
    print(row_str)

#get vector j in the matrix n
def get_vector(n,i):
    return [n[i][j] for j in range(len(n))]

#vector addition
def vector_add(a,b):
    return [a[i] + b[i] for i in range(len(a))]

#vector substraction
def vector_sub(a,b):
    return [a[i] - b[i] for i in range(len(a))]

#vector multiplication with a constant
def vector_mult_const(v,k):
    return [v[i] * k for i in range(len(v))]

#set the k-th row of matrix n to the vector v
def set_matrix_vector(n,k,v):
    col = len(n)
    for i in range(col):
        n[k][i] = v[i]

#norml2 : square of the L2-norm of the vector x
def norml2(a):
    return scalar_product(a,a)

def round(num):
    if (num > 0):
        return int(num + Fraction(1,2))
    else :
        return int(num - Fraction(1,2))

def create_matrix(n):
    row = len(n)
    col = len(n[0])
    res = [[Fraction(n[i][j]) for j in range(col)] for i in range(row)]
    return res

def create_vector(n):
    row = len(n)
    col = len(n[0])
    res = [[int(n[i][j]) for j in range(col)] for i in range(row)]
    join = []
    for v in res:
        long_list = map(int,v)
        int_list = [long_list]
        join.extend(int_list)
    return join

#Hadamard ratio
def hadamard_ratio(n):
    detOfLattice = abs(np.linalg.det(n))
    mult = 1
    for v in n:
        mult = mult * np.linalg.norm(v)
    hratio = (detOfLattice / mult) ** (1.0/len(n))
    return hratio

#Solve CVP
def solve_cvp(b,n):
    lin_com = mat_mult(b,np.linalg.inv(n))

    koef = []
    row = len(lin_com)
    col = len(lin_com[0])
    coeff = []
    for i in lin_com[0]:
        a = round(i)
        int_coeff = [a]
        coeff.extend(int_coeff)
    koef = [coeff]
    solution = mat_mult(koef,n)
    return solution

#Gram-Schmidt algorithm
def gram_schimdt(g,m,mu,B):
    row = len(g[0])

    for i in range(row):
        # bi* = bi
        b_i = get_vector(g,i)
        b_i_star = b_i
        set_matrix_vector(m,i,b_i_star)

        for j in range(i):
            #u[i][j] = (bi, bj*)/Bj
            b_j_star = get_vector(m,j)
            b_i = get_vector(g,i)
            B[j] = norml2(b_j_star)
            mu[i][j] = Fraction(scalar_product(b_i,b_j_star),B[j])
            #bi* = bi* -u[i][j]* bj*
            b_i_star = vector_sub(b_i_star,vector_mult_const(b_j_star,mu[i][j]))
            set_matrix_vector(m,i,b_i_star)
        b_i_star = get_vector(m,i)
        #B[i] = (bi*,bi*)
        B[i] = scalar_product(b_i_star,b_i_star)

#reduce
def reduce(g,mu,k,l):
    row = len(g)
    if math.fabs(mu[k][l]) > Fraction(1,2):
        r = round(mu[k][l])
        b_k = get_vector(g,k)
        b_l = get_vector(g,l)
        #bk = bk - r*bl
        set_matrix_vector(g,k,vector_sub(b_k,vector_mult_const(b_l,r)))

        for j in range(l):
            #u[k][j] = u[k][j] - r*u[l][j]
            mu[k][j] = mu[k][j] - r * mu[l][j]
        #u[k][j] = u[k][l]-r
        mu[k][l] = mu[k][l] - r

#LLL-reduction from LLL book
def lll_reduction(n,lc = Fraction(3,4)):
    col = len(n)
    row = len(n[0])
    m = [[Fraction(0) for j in range(row)] for i in range(col)]
    mu = [[Fraction(0) for j in range(row)] for i in range(row)]
    g = [[n[i][j] for j in range(row)] for i in range(row)]
    B = [Fraction(0) for j in range(row)]

    gram_schimdt(g,m,mu,B)

    #k=2
    k = 1

    while 1:
        #1-perform(*) for l=k-1
        reduce(g,mu,k,k-1)

       
