import numpy as np
import scipy
from scipy.optimize import linprog
from pytest import approx

from simplex_networks_profile import create_matrix, pivots_col, pivots_row, find_negative_col, find_negative_row, find_pivot_col, find_pivot_row, pivot
from problem_definition_profile import add_cons, constrain, add_obj, obj, maxz, minz


if __name__ == "__main__":
    # Definimos y resolvemos problema con scipy
    c_max_obj = [-3, -5]
    A_max_obj = [[1, 0], [0, 2], [3, 2]]
    b_max_obj = [4, 12, 18]
    max_obj = -1 * linprog(c_max_obj, A_ub=A_max_obj, b_ub=b_max_obj).fun
    coeff_obj = linprog(c_max_obj, A_ub=A_max_obj, b_ub=b_max_obj).x

    # Definimos y resolvemos problema con nuestro paquete
    n_var_approx = 2
    n_cons_approx = 3
    matrix_max_approx = create_matrix(n_var_approx, n_cons_approx)
    constrain(matrix_max_approx,'1,0,L,4')
    constrain(matrix_max_approx,'0,2,L,12')
    constrain(matrix_max_approx,'3,2,L,18')
    obj(matrix_max_approx,'3,5,0')
    problem_approx = maxz(matrix_max_approx)
    max_approx = problem_approx['max']
    problem_approx.pop('max')
    coeff_approx = np.array(list(problem_approx.values()))

    assert max_approx == approx(max_obj)
    assert coeff_obj == approx(coeff_approx)
