"""
Support Vector Regression (SVR) using linear and non-linear kernels
Toy example of 1D regression using linear, polynomial and RBF kernels.
Source: http://scikit-learn.org/stable/auto_examples/svm/plot_svm_regression.html#sphx-glr-auto-examples-svm-plot-svm-regression-py
Related resources: https://github.com/tanmoyie/Operations-Research/tree/master/Machine%20Learning%20in%20Optimization
"""
print(__doc__)

import numpy as np
from sklearn.svm import SVR
import matplotlib.pyplot as plt

# #############################################################################
# Generate sample data
X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()

# #############################################################################
# Add noise to targets
y[::5] += 3 * (0.5 - np.random.rand(8))

# #############################################################################
# Fit regression model
svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)
y_rbf = svr_rbf.fit(X, y).predict(X)
y_lin = svr_lin.fit(X, y).predict(X)
y_poly = svr_poly.fit(X, y).predict(X)

# #############################################################################
# Look at the results
lw = 2
plt.show()
plt.scatter(X, y, color='black', label='data')
plt.plot(X, y_rbf, color='red', lw=3, label='RBF model')
plt.plot(X, y_lin, color='c', lw=lw, linestyle='-.', label='Linear model')
plt.plot(X, y_poly, color='navy', lw=lw, linestyle='--', label='Polynomial model')
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()