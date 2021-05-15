import numpy as np
from mex.simplex.simplex_networks import create_matrix
from mex.simplex.problem_definition import constrain, obj, minz
from mex.utils.general import generates_matrix


class Minimizer():
    """Minimize the objective function"""
    def __init__(self, A, b, c):
        self.matrix = generates_matrix(A, b, c)
        self.min = None
        self.coeff = None

    def solve(self):
        solve = minz(self.matrix)
        self.min = solve['min']
        self.coeff = np.array(list(solve.values()))[:-1]

    def get_min(self):
        return self.min

    def get_coeff(self):
        return self.coeff
