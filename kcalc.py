import numpy as np

def calculk(k1,k2,k3):
    coeff=[k1*k2*k3,k1*k2+k2*k3+k1*k3,k1+k2+k3-1]
    solution = np.roots(coeff)
    liste=[solution[0],solution[1]]
    if k1+k2+k3>1:
        k=float(round(liste[0],1))
        return (k)
    else:
        k=float(round(liste[1],1))
        return (k)

def utilite(k1,k2,k3,k):
    u1=u1.get()
    u2=u2.get()
    u3=u3.get()    
    U=k1*u1 + k2*u2 + k3*u3 + k*k1*k3*u1*u3 + k*k1*k2*u1*u2 + k*k2*k3*u2*u3 + k**2*k1*k2*k3*u1*u2*u3
    return (U)
    
