import numpy as np
from scipy.optimize import minimize

def rose(x):
    '''
    the rose function return the rosenbrock function's 
    value given the parameter x, which in our problem is 
    a 3 by 1 vector
    '''
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2+100*(x[2]-x[1]**2)**2+(1-x[1])**2

def gradient(x):
    """
    the gradient function return the value of the gradient of
    the rosenbrock function, given the input x, which is a 3 by 1 vector
    """
    return np.array([400*x[0]**3-400*x[1]*x[0]-2+2*x[0],
                     400*x[1]**3-400*x[2]*x[1]-200*x[0]**2-2+202*x[1],
                     200*x[2]-200*x[1]**2])

if __name__ == "__main__":
    n = 100
    result = np.zeros(n)
    for i in range(n):
        x_init = np.random.uniform(-200,200,3)
        result[i] = minimize(rose, x_init, method="BFGS", jac = gradient).fun
    print("the minimum function value is :"+ str(min(result)))
