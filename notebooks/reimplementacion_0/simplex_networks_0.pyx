import numpy as np
import logging


def create_matrix(variables, constraints):
    """
    Creates a matrix with enough rows for each constraint plus the objective function
    and enough columns for all the variables.
    
    Args:
    
        variables (int): number of variables.
        
        constraints (int): number of constraints.
    
    Returns:
    
        matrix (numpy array): zero matrix.
    """
    
    matrix = np.zeros((constraints + 1, variables + constraints + 2))
    
    return matrix


def pivots_col(matrix):
    """
    Checks to see if pivots are required due to negative values in right column,
    excluding the bottom value.
    
    Args:
    
        matrix (numpy array): matrix to be reviewed.
        
    Returns:
    
        Flag (bool): True or False indicating whether a negative element was found.
    """
    
    m = min(matrix[:-1, -1])
    if m >= 0:
        return False
    else:
        return True


def pivots_row(matrix):
    """
    Checks to see if pivots are required due to negative values in bottom row, 
    excluding the final value.
    
    Args:
    
        matrix (numpy array): matrix to be reviewed.
        
    Returns:
    
        Flag (bool): True or False indicating whether a negative element was found.
    """
    
    l = len(matrix[:, 0])
    m = min(matrix[l-1, :-1])
    if m >= 0:
        return False
    else:
        return True


def find_negative_col(matrix):
    """
    Finds location of negative values in right column.
    
    Args:
        
        matrix (numpy array): matrix to be reviewed.
        
    Returns:
    
        n (int): index of negative value in right column.
    """
    
    l = len(matrix[0, :])
    m = min(matrix[:-1, l-1])
    if m <= 0:
        n = np.where(matrix[:-1, l-1] == m)[0][0]
    else:
        n = None
    
    return n


def find_negative_row(matrix):
    """
    Finds location of negative values in bottom row.
    
    Args:
        
        matrix (numpy array): matrix to be reviewed.
        
    Returns:
    
        n (int): index of negative value in bottom row.
    """
    
    l = len(matrix[:,0])
    m = min(matrix[l-1,:-1])
    if m <= 0:
        n = np.where(matrix[l-1, :-1] == m)[0][0]
    else:
        n = None
    
    return n


def find_pivot_col(matrix):
    """
    Finds pivot element corresponding to a negative value in right column.
    
    Args:
    
        matrix (numpy array): matrix to be reviewed.
        
    Returns:
        
        index (int): index of most negative value.
        
        c (int): index smallest value on row.
    """
    
    total = []
    neg = find_negative_col(matrix)
    row = matrix[neg, :-1]
    m = min(row)
    c = np.where(row == m)[0][0]
    col = matrix[:-1, c]
    for i,j in zip(col, matrix[:-1,-1]):  #i for col with neg, j for right col
        if i != 0 and j/i > 0:
            total.append(j/i)
        else:
            total.append(10000) #placeholder, might need to update for large scale
    index = total.index(min(total))
    
    return [index,c]


def find_pivot_row(matrix):
    """
    Finds pivot element corresponding to a negative value in bottom row.
    
    Args:
        
        matrix (numpy array): matrix to be reviewed.
        
    Returns:
    
        index (int): index of most negative value.
        
        neg (int): index smallest value.
    """
    
    if pivots_row(matrix):
        total = []
        neg = find_negative_row(matrix)
        for i, j in zip(matrix[:-1, neg], matrix[:-1, -1]):
            if i != 0 and j/i > 0:
                total.append(j/i)
            else:
                total.append(10000) #placeholder, might need to update for large scale
        index = total.index(min(total))
        
        return [index,neg]


def pivot(row,col,matrix):
    """
    Pivot about a value to remove negative in final column or row.
    
    Args:
    
        matrix (numpy array): matrix to be reviewed.
        
        row (int): position to pivot.
        
        col (int): position to pivot.
        
    Returns:
    
        t (numpy array): updated matrix.
    """
    
    lr = len(matrix[:, 0])
    lc = len(matrix[0, :])
    t = np.zeros((lr, lc))
    pr = matrix[row, :]
    if matrix[row, col]**2 > 0:
        e = 1/matrix[row, col]
        r = pr*e
        for i in range(len(matrix[:, col])):
            k = matrix[i, :]
            c = matrix[i, col]
            if list(k) == list(pr):
                continue
            else:
                t[i, :] = list(k-r*c)
        t[row,:] = list(r)
        return t
    else:
        logging.info('Cannot pivot on this element')
