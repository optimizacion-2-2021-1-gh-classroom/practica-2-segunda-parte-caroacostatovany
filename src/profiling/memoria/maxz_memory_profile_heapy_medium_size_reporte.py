import numpy as np
from scipy.optimize import linprog
from pytest import approx

from mex.simplex.simplex_networks import create_matrix, pivots_col, pivots_row, find_negative_col, find_negative_row, find_pivot_col, find_pivot_row, pivot
from mex.simplex.problem_definition import add_cons, constrain, add_obj, obj, maxz, minz
from memory_profiler import profile

from guppy import hpy


if __name__ == "__main__":
    hp = hpy()
    hp.setrelheap()
    matrix_max_approx_1 = create_matrix(20, 30)
    
    #Restricciones 1-5:
    constrain(matrix_max_approx_1,'90.09,50.61,45.03,16.83,26.92,36.29,51.61,2.450,25.15,30.22,81.78,2.444,34.71,57.17,41.14,92.00,69.17,26.77,38.44,25.35,L,79.72')
    constrain(matrix_max_approx_1,'69.62,6.235,18.95,4.843,12.34,82.56,83.65,11.18,29.91,34.66,79.32,64.11,95.56,70.83,69.77,93.99,10.83,17.88,78.04,87.34,L,68.64')
    constrain(matrix_max_approx_1,'27.58,31.56,72.90,95.74,69.19,84.21,58.42,18.88,72.27,85.58,60.66,51.78,46.34,30.96,5.505,11.68,84.84,81.16,3.668,65.52,L,1.240')
    constrain(matrix_max_approx_1,'28.91,98.28,80.47,78.34,48.34,40.00,92.46,93.44,93.79,46.63,50.50,30.32,71.96,52.57,46.29,67.03,71.13,82.94,4.676,5.110,L,34.53')
    constrain(matrix_max_approx_1,'10.16,9.828,11.24,53.81,23.53,16.98,94.65,55.01,96.43,5.556,54.05,40.95,35.37,14.02,32.04,71.37,29.52,24.35,71.32,46.73,L,43.64')
    #Restricciones 6-10:
    constrain(matrix_max_approx_1,'70.56,93.54,27.93,95.94,91.23,8.491,78.54,7.435,85.27,32.27,97.65,34.44,97.45,77.70,86.22,3.460,52.49,59.86,6.446,20.77,L,3.692')
    constrain(matrix_max_approx_1,'30.93,40.11,9.917,22.34,2.947,8.553,85.74,31.01,4.919,12.60,3.358,89.39,50.05,25.59,13.33,75.14,57.81,14.29,88.59,24.34,L,44.21')
    constrain(matrix_max_approx_1,'7.511,72.81,19.49,55.05,86.04,36.84,7.233,67.59,92.62,24.06,15.87,45.52,75.98,71.86,64.45,15.81,57.22,84.86,28.66,7.867,L,94.85')
    constrain(matrix_max_approx_1,'62.27,38.88,82.58,84.71,68.00,97.57,36.58,11.57,73.91,75.40,65.75,7.540,52.08,96.61,9.278,60.24,59.22,6.214,63.88,68.99,L,39.16')
    constrain(matrix_max_approx_1,'73.05,10.49,93.23,91.39,63.19,47.53,20.71,14.26,51.71,71.02,11.87,61.36,97.72,70.67,28.40,73.55,33.02,81.46,67.22,85.30,L,38.43')
    #Restricciones 11-15:
    constrain(matrix_max_approx_1,'93.49,28.98,23.75,48.18,73.61,18.85,15.89,90.90,71.75,80.48,97.08,88.23,86.15,57.57,78.16,40.38,19.41,75.39,54.97,38.35,L,57.08')
    constrain(matrix_max_approx_1,'84.61,42.17,56.76,23.61,66.47,13.86,36.55,37.61,39.77,2.123,92.07,21.21,85.36,27.84,81.87,34.29,55.51,71.08,81.14,41.18,L,19.63')
    constrain(matrix_max_approx_1,'66.07,71.30,29.57,3.874,45.04,98.19,92.92,18.87,44.20,17.36,36.33,45.50,17.97,67.95,62.03,32.55,50.91,47.08,85.63,36.12,L,70.07')
    constrain(matrix_max_approx_1,'63.66,7.173,29.93,31.48,64.60,72.68,2.754,16.71,79.55,4.050,95.43,31.18,61.87,68.41,3.567,21.61,45.96,3.881,40.50,91.86,L,32.45')
    constrain(matrix_max_approx_1,'67.60,7.276,78.37,96.71,79.11,21.35,78.86,23.26,63.76,43.93,59.46,78.19,70.34,92.42,58.98,95.50,84.86,76.11,13.00,60.67,L,15.32')
    #Restricciones 16-20:
    constrain(matrix_max_approx_1,'12.17,45.38,51.97,93.29,97.74,58.34,71.99,26.91,26.85,74.88,69.95,43.51,8.723,38.97,74.16,81.20,77.52,20.84,46.12,16.24,L,49.46')
    constrain(matrix_max_approx_1,'85.82,3.365,53.87,41.57,37.04,97.64,16.76,90.16,50.49,76.92,85.17,57.76,29.29,12.79,93.86,59.50,84.81,43.91,6.931,14.25,L,54.54')
    constrain(matrix_max_approx_1,'72.94,37.67,28.00,33.56,71.22,73.32,33.33,27.54,71.75,61.17,39.68,38.85,79.89,92.34,31.80,10.18,78.30,6.469,41.89,50.98,L,24.96')
    constrain(matrix_max_approx_1,'80.03,67.82,37.00,51.50,17.85,10.91,26.95,65.79,18.51,84.34,3.196,72.33,48.76,8.459,53.13,18.23,9.679,2.543,48.12,52.09,L,11.98')
    constrain(matrix_max_approx_1,'28.10,98.61,1.938,94.54,98.78,18.29,26.88,91.15,9.967,5.279,99.44,79.94,82.80,30.05,85.13,8.410,83.47,15.45,46.43,56.54,L,1.772')
    #Restricciones 21-25:
    constrain(matrix_max_approx_1,'92.44,92.82,95.87,78.14,93.72,55.82,92.28,64.95,94.39,91.63,20.11,32.16,10.08,23.98,9.257,71.39,48.74,60.76,96.93,56.57,L,50.61')
    constrain(matrix_max_approx_1,'22.14,72.51,48.51,98.13,90.25,85.24,1.804,28.47,45.93,36.05,35.43,7.104,70.67,97.69,74.87,39.72,13.98,58.00,2.024,85.30,L,94.20')
    constrain(matrix_max_approx_1,'72.16,93.13,45.85,76.06,22.53,36.16,81.15,92.51,97.12,67.37,37.37,69.21,72.32,63.23,92.90,61.86,11.42,34.15,49.78,6.688,L,97.49')
    constrain(matrix_max_approx_1,'58.39,34.12,77.96,5.433,83.02,84.14,59.82,22.39,70.75,19.67,24.53,41.00,56.24,89.32,14.63,77.15,34.12,34.28,55.17,31.45,L,34.16')
    constrain(matrix_max_approx_1,'20.15,1.416,74.34,23.20,8.632,71.47,32.10,59.23,91.44,37.58,23.29,39.11,19.54,3.000,2.319,43.50,35.17,66.78,40.41,50.82,L,6.26')
    #Restricciones 26-30:
    constrain(matrix_max_approx_1,'54.65,70.46,46.30,66.92,27.45,25.48,81.67,96.67,42.57,43.22,43.29,60.58,19.07,27.73,92.63,60.94,84.33,8.800,78.62,17.94,L,70.31')
    constrain(matrix_max_approx_1,'83.10,98.45,22.09,36.01,39.99,6.380,28.27,10.69,57.29,63.19,44.42,51.00,15.57,11.27,63.56,17.54,40.71,47.53,27.81,27.66,L,79.18')
    constrain(matrix_max_approx_1,'22.20,29.98,87.02,25.26,47.23,55.22,83.70,88.56,67.82,6.36,66.62,3.853,47.37,97.22,83.37,89.41,61.79,96.26,91.11,79.89,L,44.51')
    constrain(matrix_max_approx_1,'6.828,84.55,80.55,86.10,54.30,18.86,80.63,54.07,63.94,89.28,64.89,87.44,13.06,31.29,63.10,75.33,21.06,61.33,1.093,91.08,L,53.22')
    constrain(matrix_max_approx_1,'85.33,57.98,42.51,53.95,10.49,32.74,43.28,51.52,89.99,43.97,46.69,44.05,85.91,19.12,23.85,58.82,71.23,8.885,18.81,87.44,L,50.65')
    #Función objetivo:
    obj(matrix_max_approx_1,'52.16,45.51,69.09,84.88,38.73,84.47,97.50,61.32,16.27,36.42,77.24,36.91,62.85,50.77,81.22,66.94,31.10,45.05,37.68,40.76,0')
    problem_approx_1 = maxz(matrix_max_approx_1)
    max_approx_1 = problem_approx_1['max']
    problem_approx_1.pop('max')
    coeff_approx_1 = np.array(list(problem_approx_1.values()))
    
    h = hp.heap()
    print(h)
    
    
    c_max_obj = [-52.16, -45.51, -69.09, -84.88, -38.73,
                  -84.47, -97.50, -61.32, -16.27, -36.42,
                  -77.24, -36.91, -62.85, -50.77, -81.22,
                  -66.94, -31.10, -45.05, -37.68, -40.76]
    
    A_max_obj = [[90.09, 50.61, 45.03, 16.83, 26.92,
                36.29, 51.61, 2.450, 25.15, 30.22,
                81.78, 2.444, 34.71, 57.17, 41.14,
                92.00, 69.17, 26.77, 38.44, 25.35], 
               
               [69.62, 6.235, 18.95, 4.843, 12.34,
                82.56, 83.65, 11.18, 29.91, 34.66,
                79.32, 64.11, 95.56, 70.83, 69.77,
                93.99, 10.83, 17.88, 78.04, 87.34],
               
               [27.58, 31.56, 72.90, 95.74, 69.19,
                84.21, 58.42, 18.88, 72.27, 85.58,
                60.66, 51.78, 46.34, 30.96, 5.505,
                11.68, 84.84, 81.16, 3.668, 65.52],
               
               [28.91, 98.28, 80.47, 78.34, 48.34,
                40.00, 92.46, 93.44, 93.79, 46.63,
                50.50, 30.32, 71.96, 52.57, 46.29,
                67.03, 71.13, 82.94, 4.676, 5.110],
               
               [10.16, 9.828, 11.24, 53.81, 23.53,
                16.98, 94.65, 55.01, 96.43, 5.556,
                54.05, 40.95, 35.37, 14.02, 32.04,
                71.37, 29.52, 24.35, 71.32, 46.73],
               
               [70.56, 93.54, 27.93, 95.94, 91.23,
                8.491, 78.54, 7.435, 85.27, 32.27,
                97.65, 34.44, 97.45, 77.70, 86.22,
                3.460, 52.49, 59.86, 6.446, 20.77],
               
               [30.93, 40.11, 9.917, 22.34, 2.947,
                8.553, 85.74, 31.01, 4.919, 12.60,
                3.358, 89.39, 50.05, 25.59, 13.33,
                75.14, 57.81, 14.29, 88.59, 24.34],
               
               [7.511, 72.81, 19.49, 55.05, 86.04,
                36.84, 7.233, 67.59, 92.62, 24.06,
                15.87, 45.52, 75.98, 71.86, 64.45,
                15.81, 57.22, 84.86, 28.66, 7.867],
               
               [62.27, 38.88, 82.58, 84.71, 68.00,
                97.57, 36.58, 11.57, 73.91, 75.40,
                65.75, 7.540, 52.08, 96.61, 9.278,
                60.24, 59.22, 6.214, 63.88, 68.99],
               
               [73.05, 10.49, 93.23, 91.39, 63.19,
                47.53, 20.71, 14.26, 51.71, 71.02,
                11.87, 61.36, 97.72, 70.67, 28.40,
                73.55, 33.02, 81.46, 67.22, 85.30],
               
               [93.49, 28.98, 23.75, 48.18, 73.61,
                18.85, 15.89, 90.90, 71.75, 80.48,
                97.08, 88.23, 86.15, 57.57, 78.16,
                40.38, 19.41, 75.39, 54.97, 38.35],
               
               [84.61, 42.17, 56.76, 23.61, 66.47,
                13.86, 36.55, 37.61, 39.77, 2.123,
                92.07, 21.21, 85.36, 27.84, 81.87,
                34.29, 55.51, 71.08, 81.14, 41.18], 
               
               [66.07, 71.30, 29.57, 3.874, 45.04,
                98.19, 92.92, 18.87, 44.20, 17.36,
                36.33, 45.50, 17.97, 67.95, 62.03,
                32.55, 50.91, 47.08, 85.63, 36.12], 
               
               [63.66, 7.173, 29.93, 31.48, 64.60,
                72.68, 2.754, 16.71, 79.55, 4.050,
                95.43, 31.18, 61.87, 68.41, 3.567,
                21.61, 45.96, 3.881, 40.50, 91.86], 
               
               [67.60, 7.276, 78.37, 96.71, 79.11,
                21.35, 78.86, 23.26, 63.76, 43.93,
                59.46, 78.19, 70.34, 92.42, 58.98,
                95.50, 84.86, 76.11, 13.00, 60.67],
               
               [12.17, 45.38, 51.97, 93.29, 97.74,
                58.34, 71.99, 26.91, 26.85, 74.88,
                69.95, 43.51, 8.723, 38.97, 74.16,
                81.20, 77.52, 20.84, 46.12, 16.24],
               
               [85.82, 3.365, 53.87, 41.57, 37.04,
                97.64, 16.76, 90.16, 50.49, 76.92,
                85.17, 57.76, 29.29, 12.79, 93.86,
                59.50, 84.81, 43.91, 6.931, 14.25],
               
               [72.94, 37.67, 28.00, 33.56, 71.22,
                73.32, 33.33, 27.54, 71.75, 61.17,
                39.68, 38.85, 79.89, 92.34, 31.80,
                10.18, 78.30, 6.469, 41.89, 50.98],
               
               [80.03, 67.82, 37.00, 51.50, 17.85,
                10.91, 26.95, 65.79, 18.51, 84.34,
                3.196, 72.33, 48.76, 8.459, 53.13,
                18.23, 9.679, 2.543, 48.12, 52.09],
               
               [28.10, 98.61, 1.938, 94.54, 98.78,
                18.29, 26.88, 91.15, 9.967, 5.279,
                99.44, 79.94, 82.80, 30.05, 85.13,
                8.410, 83.47, 15.45, 46.43, 56.54],
               
               [92.44, 92.82, 95.87, 78.14, 93.72,
                55.82, 92.28, 64.95, 94.39, 91.63,
                20.11, 32.16, 10.08, 23.98, 9.257,
                71.39, 48.74, 60.76, 96.93, 56.57],
               
               [22.14, 72.51, 48.51, 98.13, 90.25,
                85.24, 1.804, 28.47, 45.93, 36.05,
                35.43, 7.104, 70.67, 97.69, 74.87,
                39.72, 13.98, 58.00, 2.024, 85.30],
               
               [72.16, 93.13, 45.85, 76.06, 22.53,
                36.16, 81.15, 92.51, 97.12, 67.37,
                37.37, 69.21, 72.32, 63.23, 92.90,
                61.86, 11.42, 34.15, 49.78, 6.688],
               
               [58.39, 34.12, 77.96, 5.433, 83.02,
                84.14, 59.82, 22.39, 70.75, 19.67,
                24.53, 41.00, 56.24, 89.32, 14.63,
                77.15, 34.12, 34.28, 55.17, 31.45],
               
               [20.15, 1.416, 74.34, 23.20, 8.632,
                71.47, 32.10, 59.23, 91.44, 37.58,
                23.29, 39.11, 19.54, 3.000, 2.319,
                43.50, 35.17, 66.78, 40.41, 50.82],
               
               [54.65, 70.46, 46.30, 66.92, 27.45,
                25.48, 81.67, 96.67, 42.57, 43.22,
                43.29, 60.58, 19.07, 27.73, 92.63,
                60.94, 84.33, 8.800, 78.62, 17.94],
               
               [83.10, 98.45, 22.09, 36.01, 39.99,
                6.380, 28.27, 10.69, 57.29, 63.19,
                44.42, 51.00, 15.57, 11.27, 63.56,
                17.54, 40.71, 47.53, 27.81, 27.66],
               
               [22.20, 29.98, 87.02, 25.26, 47.23,
                55.22, 83.70, 88.56, 67.82, 6.36,
                66.62, 3.853, 47.37, 97.22, 83.37,
                89.41, 61.79, 96.26, 91.11, 79.89],
               
               [6.828, 84.55, 80.55, 86.10, 54.30,
                18.86, 80.63, 54.07, 63.94, 89.28,
                64.89, 87.44, 13.06, 31.29, 63.10,
                75.33, 21.06, 61.33, 1.093, 91.08],
               
               [85.33, 57.98, 42.51, 53.95, 10.49,  
                32.74, 43.28, 51.52, 89.99, 43.97,
                46.69, 44.05, 85.91, 19.12, 23.85,
                58.82, 71.23, 8.885, 18.81, 87.44]]
    b_max_obj = [79.72, 68.64, 1.240, 34.53, 43.64, 3.692, 44.21, 94.85, 39.16, 38.43,
               57.08, 19.63, 70.07, 32.45, 15.32, 49.46, 54.54, 24.96, 11.98, 1.772,
               50.61, 94.20, 97.49, 34.16, 6.26, 70.31, 79.18, 44.51, 53.22, 50.65]
    
    max_obj = -1*linprog(c_max_obj, A_ub=A_max_obj, b_ub=b_max_obj).fun
    coeff_obj = linprog(c_max_obj, A_ub=A_max_obj, b_ub=b_max_obj).x
    
    
    assert max_approx_1 == approx(max_obj)
    assert np.round(coeff_obj,2) == approx(np.round(coeff_obj,2))