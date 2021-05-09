
from scipy.optimize import linprog
from pytest import approx

from mex.simplex.maximizer_class import Maximizer


if __name__ == "__main__":
    # Definimos y resolvemos problema con scipy
    c_max_obj = [-3, -5]
    A_max_obj = [[1, 0], [0, 2], [3, 2]]
    b_max_obj = [4, 12, 18]
    max_obj = -1 * linprog(c_max_obj, A_ub=A_max_obj, b_ub=b_max_obj).fun
    coeff_obj = linprog(c_max_obj, A_ub=A_max_obj, b_ub=b_max_obj).x

    # Definimos y resolvemos problema con nuestro paquete
    maxim = Maximizer(2, 3)
    maxim.add_constraint('1,0,L,4')
    maxim.add_constraint('0,2,L,12')
    maxim.add_constraint('3,2,L,18')
    maxim.add_objective('3,5,0')
    maxim.solve()
    max_approx = maxim.get_max()
    coeff_approx = maxim.get_coeff()

    assert max_approx == approx(max_obj)
    assert coeff_obj == approx(coeff_approx)
