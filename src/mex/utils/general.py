import numpy as np


def convert_min(matrix):
    """
    This function multiplies by -1 the objective function for maximization problems. This is because
    if the problem to be solved is maximization then it is analogue to solve the problem -minimization.
    
    Args:
    
        matrix (numpy array): matrix to be updated.
    
    Returns:
    
        matrix (numpy array): matrix multiplied by -1.
    """
    
    matrix[-1, :-2] = [-1*i for i in matrix[-1, :-2]]
    matrix[-1, -1] = -1*matrix[-1, -1]
    
    return matrix


def gen_var(lc, lr):
    """
    Generates the required number of variables. They are defined by the problem.
    
    Args:
    
        lc : number of columns
        lr : number of rows
    
    Returns:
    
        v (list): list with problem variables.
    """
    
    var = lc - lr - 1
    v = []
    
    for i in range(var):
        v.append('x' + str(i+1))
    
    return v


def convert(eq):
    """
    Converts equation into a list containing the coefficients of the equation.
    
    Args:
    
        eq (string): equation defined with :func:`constrain`.
    
    Returns:
    
        eq (list): list with equation coefficients.
    """
    
    eq = eq.split(',')
    
    if 'G' in eq:
        g = eq.index('G')
        del eq[g]
        eq = [float(i)*-1 for i in eq]
        return eq
    
    if 'L' in eq:
        l = eq.index('L')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq
    
    if 'E' in eq:
        l = eq.index('E')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq


def generates_matrix(A_matrix, b_vector, c_vector):
    """
    Generate matrix of a problem:
    Ax <= b

    Args:

        A_matrix (matrix):
        b_vector (vector):
        c_vector (vector):

    Returns:

        A_new (matrix):
    """

    # Concatenar A_new con c de forma rbind
    A_new = np.vstack([A_matrix, np.transpose(c_vector)])

    nrow, ncol = A_new.shape
    # Generar la matriz de pivoteo
    I = np.eye(nrow, nrow)
    # Crear nuevo vector de restricciones
    b_new = np.concatenate([b_vector, np.array([0])], axis=0)

    # Concatenar A_new, b_new de forma cbind
    A_new = np.c_[A_new, I, b_new]

    return A_new
