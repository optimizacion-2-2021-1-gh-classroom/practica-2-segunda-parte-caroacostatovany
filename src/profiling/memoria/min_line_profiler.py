
from scipy.optimize import linprog
from pytest import approx

from mex.simplex.minimzer_class import Minimzer

if __name__ == "__main__":
    # Definimos y resolvemos problema con scipy
    c_min_obj = [-1, -3]
    A_min_obj = [[1, 1], [-1, 2]]
    b_min_obj = [6, 8]
    min_obj = linprog(c_min_obj, A_ub=A_min_obj, b_ub=b_min_obj).fun
    coeff_obj = linprog(c_min_obj, A_ub=A_min_obj, b_ub=b_min_obj).x

    # Definimos y resolvemos problema con nuestro paquete
    minim = Minimzer(2, 2)
    minim.add_constraint('1,1,L,6')
    minim.add_constraint('-1,2,L,8')
    minim.add_objective('-1,-3,0')
    minim.solve()
    min_approx = minim.get_min()
    coeff_approx = minim.get_coeff()

    assert min_approx == approx(min_obj)
    assert coeff_obj == approx(coeff_approx)
