import numpy as np
from scipy.optimize import linprog
from pytest import approx

from mex.simplex.minimzer_class import Minimzer

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
    minim = Minimzer(7, 7)
    minim.add_constraint('1,1,1,0,0,0,0,E,50')
    minim.add_constraint('-1,0,0,1,0,0,0,E,40')
    minim.add_constraint('0,-1,0,-1,1,0,0,E,0')
    minim.add_constraint('0,0,-1,0,0,1,-1,E,-30')
    minim.add_constraint('0,0,0,0,-1,-1,1,E,-60')
    minim.add_constraint('1,0,0,0,0,0,0,L,10')
    minim.add_constraint('0,0,0,0,1,0,0,L,80')
    minim.add_objective('2,4,9,3,1,3,2,0')
    minim.solve()
    net_approx = minim.get_min()
    net_coeff_approx = minim.get_coeff()

    assert net_obj == approx(net_approx)
    assert np.round(net_coeff_obj, 0) == approx(net_coeff_approx)
