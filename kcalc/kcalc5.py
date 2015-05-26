import numpy as np
from sympy import *

def calculk5(k1,k2,k3,k4,k5):
    k = symbols('k')
    solution=solve(k1*k2*k3*k4*k5*k**4+(k1*k2*k3*k5 + k1*k2*k4*k5 + k2*k3*k4*k5 + k1*k3*k4*k5 + k1*k2*k3*k4)*k**3+(k1*k2*k3 + k1*k2*k4 + k1*k2*k5 + k1*k3*k4 +k1*k3*k5 + k1*k4*k5 + k2*k3*k4 + k2*k3*k5 + k2*k4*k5 + k3*k4*k5)*k**2+ (k2*k3 + k1*k3 + k1*k4 + k2*k4 + k3*k4 + k1*k2 + k1*k5 + k2*k5 + k3*k5 + k4*k5)*k + k1+k2+k3+k4+k5-1, k)
       
    return (solution)

    
def utilite(k1,k2,k3,k4,k):
    u1=u1.get()
    u2=u2.get()
    u3=u3.get()    
    u4=u4.get()
    u5=u5.get()
    U= k^4*k1*k2*k3*k4*k5*u1*u2*u3*u4*u5 + k^3(k1*k2*k3*k5*u1*u2*u3*u5 + k1*k2*k4*k5*u1*u2*u4*u5 + k2*k3*k4*k5*u2*u3*u5*u4 + k1*k3*k4*k5*u1*u5*u3*u4 + k1*k2*k3*k4*u1*u2*u3*u4) + k**(k1*k2*k3*u1*u2*u3 + k1*k2*k4*u1*u2*u4 + k1*k2*k5*u1*u2*u5 + k1*k3*k4*u1*u3*u4 +k1*k3*k5*u1*u3*u5 + k1*k4*k5*u1*u4*u5 + k2*k3*k4*u2*u3*u4 + k2*k3*k5*u2*u3*u5 + k2*k4*k5*u2*u4*u5 + k3*k4*k5*u3*u4*u5) + k(k2*k3*u2*u3 + k1*k3*u1*u3 + k1*k4*u4*u4 + k2*k4*u2*u4 + k3*k4*u3*u4 + k1*k2*u1*u2 + k1*k5*u1*u5 + k2*k5*u2*u5 + k3*k5*u3*u5 + k4*k5*u4*u5) + k1*u1 + k2*u2 + k3*u3 + k4*u4 + k5*u5
    return (U)
