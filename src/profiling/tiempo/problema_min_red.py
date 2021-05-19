import numpy as np
from scipy.optimize import linprog
from pytest import approx

from simplex_networks_profile import create_matrix, pivots_col, pivots_row, find_negative_col, find_negative_row, find_pivot_col, find_pivot_row, pivot
from problem_definition_profile import add_cons, constrain, add_obj, obj, maxz, minz

if __name__ == "__main__":
    # Definimos y resolvemos problema con scipy
    c_net_obj = [2, 4, 9, 3, 1, 3, 2]
    A_ub_net_obj = [[1, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1, 0, 0]]
    b_ub_net_obj = [10, 80]
    A_eq_net_obj = [[1, 1, 1, 0, 0, 0, 0],
                    [-1, 0, 0, 1, 0, 0, 0],
                    [0, -1, 0, -1, 1, 0, 0],
                    [0, 0, -1, 0, 0, 1, -1],
                    [0, 0, 0, 0, -1, -1, 1]]
    b_eq_net_obj = [50, 40, 0, -30, -60]
    net_obj = linprog(c_net_obj, A_ub=A_ub_net_obj, b_ub=b_ub_net_obj, A_eq=A_eq_net_obj, b_eq=b_eq_net_obj).fun
    net_coeff_obj = linprog(c_net_obj, A_ub=A_ub_net_obj, b_ub=b_ub_net_obj, A_eq=A_eq_net_obj, b_eq=b_eq_net_obj).x

    # Definimos y resolvemos problema con nuestro paquete
    n_var_approx = 7
    n_cons_approx = 7
    matrix_net_approx = create_matrix(n_var_approx, n_cons_approx)
    constrain(matrix_net_approx,'1,1,1,0,0,0,0,E,50')
    constrain(matrix_net_approx,'-1,0,0,1,0,0,0,E,40')
    constrain(matrix_net_approx,'0,-1,0,-1,1,0,0,E,0')
    constrain(matrix_net_approx,'0,0,-1,0,0,1,-1,E,-30')
    constrain(matrix_net_approx,'0,0,0,0,-1,-1,1,E,-60')
    constrain(matrix_net_approx,'1,0,0,0,0,0,0,L,10')
    constrain(matrix_net_approx,'0,0,0,0,1,0,0,L,80')
    obj(matrix_net_approx,'2,4,9,3,1,3,2,0')
    problem_approx = minz(matrix_net_approx)
    net_approx = problem_approx['min']
    problem_approx.pop('min')
    net_coeff_approx = np.array(list(problem_approx.values()))

    assert net_obj == approx(net_approx)
    assert np.round(net_coeff_obj, 0) == approx(net_coeff_approx)
