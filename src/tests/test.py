import numpy as np
from pytest import approx
from scipy.optimize import linprog

#import os
#os.chdir("..")
from mex.simplex.simplex_networks import create_matrix
from mex.simplex.problem_definition import constrain, obj, minz, maxz
from mex.simplex.minimizer_class import Minimizer
from mex.simplex.maximizer_class import Maximizer

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
    minim = Minimizer(A_min_obj, b_min_obj, c_min_obj)
    #minim.add_constraint('1,1,L,6')
    #minim.add_constraint('-1,2,L,8')
    #minim.add_objective('-1,-3,0')
    minim.solve()
    min_approx = minim.get_min()
    coeff_approx = minim.get_coeff()

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
    maxim = Maximizer(A_max_obj, b_max_obj, c_max_obj)
    #maxim.add_constraint('1,0,L,4')
    #maxim.add_constraint('0,2,L,12')
    #maxim.add_constraint('3,2,L,18')
    #maxim.add_objective('3,5,0')
    maxim.solve()
    max_approx = maxim.get_max()
    coeff_approx = maxim.get_coeff()

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
    minim = Minimizer(A_eq_net_obj, b_eq_net_obj, c_net_obj)
    #minim.add_constraint('1,1,1,0,0,0,0,E,50')
    #minim.add_constraint('-1,0,0,1,0,0,0,E,40')
    #minim.add_constraint('0,-1,0,-1,1,0,0,E,0')
    #minim.add_constraint('0,0,-1,0,0,1,-1,E,-30')
    #minim.add_constraint('0,0,0,0,-1,-1,1,E,-60')
    #minim.add_constraint('1,0,0,0,0,0,0,L,10')
    #minim.add_constraint('0,0,0,0,1,0,0,L,80')
    #minim.add_objective('2,4,9,3,1,3,2,0')
    minim.solve()
    net_approx = minim.get_min()
    net_coeff_approx = minim.get_coeff()

    assert net_obj == approx(net_approx)
    assert np.round(net_coeff_obj, 0) == approx(net_coeff_approx)
