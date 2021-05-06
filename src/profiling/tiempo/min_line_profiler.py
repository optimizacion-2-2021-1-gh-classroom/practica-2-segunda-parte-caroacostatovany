
import numpy as np
import scipy
from scipy.optimize import linprog
from pytest import approx

from mex.simplex.simplex_networks import create_matrix, pivots_col, pivots_row, find_negative_col, find_negative_row, \
    find_pivot_col, find_pivot_row, pivot
from mex.simplex.problem_definition import add_cons, constrain, add_obj, obj, maxz, minz


if __name__ == "__main__":
    # Definimos y resolvemos problema con scipy
    c_min_obj = [-1, -3]
    A_min_obj = [[1, 1], [-1, 2]]
    b_min_obj = [6, 8]
    min_obj = linprog(c_min_obj, A_ub=A_min_obj, b_ub=b_min_obj).fun
    coeff_obj = linprog(c_min_obj, A_ub=A_min_obj, b_ub=b_min_obj).x

    # Definimos y resolvemos problema con nuestro paquete
    n_var_approx = 2
    n_cons_approx = 2
    matrix_min_approx = create_matrix(n_var_approx, n_cons_approx)
    constrain(matrix_min_approx, '1,1,L,6')
    constrain(matrix_min_approx, '-1,2,L,8')
    obj(matrix_min_approx, '-1,-3,0')
    problem_approx = minz(matrix_min_approx)
    min_approx = problem_approx['min']
    problem_approx.pop('min')
    coeff_approx = np.array(list(problem_approx.values()))

    assert min_approx == approx(min_obj)
    assert coeff_obj == approx(coeff_approx)
    