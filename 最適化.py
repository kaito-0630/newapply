import streamlit as st
from scipy.optimize import minimize
import numpy as np

def optimize_function(x):
    return x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]

def optimize():
    st.title("Optimization App")

    x0 = np.array([1,1,1,1])
    bounds = [(0, None), (0, None), (0, None), (0, None)]


    method = st.selectbox("Select optimization method", ["BFGS", "L-BFGS-B", "SLSQP"])

    result = minimize(optimize_function, x0, bounds=bounds, method=method)

    st.write("Minimum value:", result.fun)
    st.write("Optimized values:", result.x)

if __name__ == '__main__':
    optimize()




