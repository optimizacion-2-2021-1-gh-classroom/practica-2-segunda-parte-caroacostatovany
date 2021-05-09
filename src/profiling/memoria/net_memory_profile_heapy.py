import numpy as np
from scipy.optimize import linprog
from pytest import approx

from mex.simplex.simplex_networks import create_matrix, pivots_col, pivots_row, find_negative_col, find_negative_row, find_pivot_col, find_pivot_row, pivot
from mex.simplex.problem_definition import add_cons, constrain, add_obj, obj, maxz, minz
from memory_profiler import profile

from guppy import hpy

hp = hpy()
hp.setrelheap()
matrix_max_approx_1 = create_matrix(7,7)
constrain(matrix_max_approx_1, '1,1,1,0,0,0,0,E,50')
constrain(matrix_max_approx_1, '-1,0,0,1,0,0,0,E,40')
constrain(matrix_max_approx_1, '0,-1,0,-1,1,0,0,E,0')
constrain(matrix_max_approx_1, '0,0,-1,0,0,1,-1,E,-30')
constrain(matrix_max_approx_1, '0,0,0,0,-1,-1,1,E,-60')
constrain(matrix_max_approx_1, '1,0,0,0,0,0,0,L,10')
constrain(matrix_max_approx_1, '0,0,0,0,1,0,0,L,80')
obj(matrix_max_approx_1, '2,4,9,3,1,3,2,0')
problem_approx_1 = minz(matrix_max_approx_1)

h = hp.heap()
print(h)