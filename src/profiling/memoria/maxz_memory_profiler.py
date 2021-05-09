import numpy as np
from scipy.optimize import linprog
from pytest import approx

from mex.simplex.simplex_networks import create_matrix, pivots_col, pivots_row, find_negative_col, find_negative_row, find_pivot_col, find_pivot_row, pivot
from mex.simplex.problem_definition import add_cons, constrain, add_obj, obj, maxz, minz

@profile
def profiling_memory_example(matrix, aux=True):
    """
    Realizar todo el proceso del problema a resolver de optimización con el método Simplex
    """
    constrain(matrix, '1,0,L,4')
    constrain(matrix, '0,2,L,12')
    constrain(matrix, '3,2,L,18')
    obj(matrix, '3,5,0')
    problem_approx_1 = maxz(matrix)
    max_approx_1 = problem_approx_1['max']
    problem_approx_1.pop('max')
    coeff_approx_1 = np.array(list(problem_approx_1.values()))

    return max_approx_1, coeff_approx_1

if __name__ == "__main__":
    # Paquete scipy
    c_max_obj_1 = [-3, -5]
    A_max_obj_1 = [[1, 0], [0, 2], [3, 2]]
    b_max_obj_1 = [4, 12, 18]

    max_obj_1 = -1 * linprog(c_max_obj_1, A_ub=A_max_obj_1, b_ub=b_max_obj_1).fun
    coeff_obj_1 = linprog(c_max_obj_1, A_ub=A_max_obj_1, b_ub=b_max_obj_1).x

    # Paquete mex
    matrix_max_approx_1 = create_matrix(2, 3)
    max_approx_1, coeff_approx_1 = profiling_memory_example(matrix_max_approx_1)

    print("El valor objetivo obtenido con scipy es: ", max_obj_1)
    print("El valor aproximado obtenido con mex es: ", max_approx_1)
    print("Los coeficientes objetivos obtenidos con scipy son: ", coeff_obj_1)
    print("Los coeficientes aproximados obtenidos con mex son: ", coeff_approx_1)