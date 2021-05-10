import numpy as np
from scipy.optimize import linprog
from pytest import approx

from mex.simplex.simplex_networks import create_matrix, pivots_col, pivots_row, find_negative_col, find_negative_row, find_pivot_col, find_pivot_row, pivot
from mex.simplex.problem_definition import add_cons, constrain, add_obj, obj, maxz, minz
from memory_profiler import profile

from guppy import hpy

hp = hpy()
hp.setrelheap()
matrix_max_approx_1 = create_matrix(2, 2)
constrain(matrix_max_approx_1, '1,1,L,6')
constrain(matrix_max_approx_1, '-1,2,L,8')
obj(matrix_max_approx_1, '-1,-3,0')
problem_approx_1 = minz(matrix_max_approx_1)

h = hp.heap()
print(h)