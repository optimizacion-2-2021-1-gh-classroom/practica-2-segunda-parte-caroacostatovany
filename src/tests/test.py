import numpy as np
from pytest import approx
from scipy.optimize import linprog

#import os
#os.chdir("..")
from mex.simplex.simplex_networks import create_matrix
from mex.simplex.problem_definition import constrain, obj, minz, maxz


def test_min_problem():
    """
    This function will test a minimization problem
    """
    
    # Definimos y resolvemos problema con scipy
    c_min_obj = [-1, -3]
    A_min_obj = [[1, 1], [-1, 2]]
    b_min_obj = [6, 8]
    min_obj = linprog(c_min_obj, A_ub = A_min_obj, b_ub = b_min_obj).fun
    coeff_obj = linprog(c_min_obj, A_ub = A_min_obj, b_ub = b_min_obj).x
    
    # Definimos y resolvemos problema con nuestro paquete
    n_var_approx = 2
    n_cons_approx = 2
    matrix_min_approx = create_matrix(n_var_approx,n_cons_approx)
    constrain(matrix_min_approx,'1,1,L,6')
    constrain(matrix_min_approx,'-1,2,L,8')
    obj(matrix_min_approx,'-1,-3,0')
    problem_approx = minz(matrix_min_approx)
    min_approx = problem_approx['min']
    problem_approx.pop('min')
    coeff_approx = np.array(list(problem_approx.values()))
    
    assert min_approx == approx(min_obj)
    assert coeff_obj == approx(coeff_approx)
    

    
def test_max_problem():
    """
    This function will test a maximization problem
    """
    
    # Definimos y resolvemos problema con scipy
    c_max_obj = [-3, -5]
    A_max_obj = [[1, 0], [0, 2], [3, 2]]
    b_max_obj = [4, 12, 18]
    max_obj = -1*linprog(c_max_obj, A_ub=A_max_obj, b_ub=b_max_obj).fun
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

    
def test_net_problem():
    """
    This function will test a minimum cost network flow problem
    """
    
    # Definimos y resolvemos problema con scipy
    c_net_obj = [2,4,9,3,1,3,2]
    A_ub_net_obj = [[1,0,0,0,0,0,0],
                [0,0,0,0,1,0,0]]
    b_ub_net_obj = [10,80]
    A_eq_net_obj = [[1,1,1,0,0,0,0],
             [-1,0,0,1,0,0,0],
             [0,-1,0,-1,1,0,0],
             [0,0,-1,0,0,1,-1],
             [0,0,0,0,-1,-1,1]]
    b_eq_net_obj = [50,40,0,-30,-60]
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
    assert np.round(net_coeff_obj,0) == approx(net_coeff_approx)