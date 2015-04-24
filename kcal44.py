import numpy as np

def calculk4(k1,k2,k3,k4):
    coeff=[k1*k2*k3*k4,k1*k2*k3+k1*k2*k4+k2*k3*k4+k1*k3*k4,k1*k2+k2*k3+k1*k3+k1*k4+k2*k4+k3*k4,k1+k2+k3+k4-1]
    solution = cardan(coeff)
    liste=[solution[0],solution[1], solution[2]]
    k=min(abs(round((liste),1)))
    return (k)

def utilite(k1,k2,k3,k4,k):
    u1=u1.get()
    u2=u2.get()
    u3=u3.get()    
    u4=u4.get()
    U=k^3*k1*k2*k3*k4*u1*u2*u3*u4+k^2*(k1*k2*k3*u1*u2*u3+k1*k2*k4*u1*u2*u4+k2*k3*k4*u2*u3*u4+k1*k3*k4*u1*u3*u4)+k*(k1*k2*u1*u2+k2*k3*u2*u3+k1*k3*u1*u3+k1*k4*u1*u4+k2*k4*u2*u4+k3*k4*u3*u4)+k1*u1+k2*u2+k3*u3+k4*u4
    return (U)
