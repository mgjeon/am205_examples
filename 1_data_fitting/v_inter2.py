#!/usr/bin/python3
from math import *
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate a polynomial
def f(xx,b):
    z=b[0]
    for i in range(1,n):
        z*=xx
        z+=b[i]
    return z

# Initialize x points and function values
n=12
x=np.linspace(0,3,n)
y=np.array([exp(-q) for q in x])

# Solve Vandermonde problem
V=np.vander(x)
b=np.linalg.solve(V,y)

# Add optional random perturbation
b+=1e-6*np.random.rand(n)

# Plot interpolant
xx=np.linspace(0,3,301)
yy=np.array([f(q,b) for q in xx])
yy2=np.array([exp(-q) for q in xx])
yy3=np.array([f(q,b)-exp(-q) for q in xx])

# Plot figure using Matplotlib
# plt.figure()
# plt.plot(xx,yy,label="Interpolant")
# plt.plot(xx,yy2,label="exp(-x)")
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()

plt.figure()
plt.plot(xx,yy3,label="Difference")
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

