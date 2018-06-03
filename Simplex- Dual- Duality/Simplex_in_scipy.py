"""
Related YouTube Video: https://www.youtube.com/watch?v=e2lHyMl1IYY&index=2&list=PLHyZ7Tamw-fevmrx2V3U13hPDDlUSBbi7 
"""
import numpy as np
import scipy as sp

c = [-3, -5]
A = [[1, 0], [0, 2], [3, 2]]
b = [4, 12, 18]
x0_bounds = (0, None)
x1_bounds = (0, None)

from scipy.optimize import linprog
# Solve the problem by Simplex method in Optimization
res = linprog(c, A_ub=A, b_ub=b,  bounds=(x0_bounds, x1_bounds), method='simplex', options={"disp": True})
print(res)
