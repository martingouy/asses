import numpy as np
import math
import json
from sympy import *
from scipy.optimize import fsolve

def calculUtilityMultiplicative(myK, myU):
    print("utility Multiplicative")
    if len(myK)-1==2:
        return {'U':utilite2(myK[0]['value'],myK[1]['value'],myK[2]['value'],convert_to_text(myU[0],"x1"),convert_to_text(myU[1], "x2")), 'k':myK, 'utilities':myU}
    elif len(myK)-1==3:
        return {'U':utilite3(myK[0]['value'],myK[1]['value'],myK[2]['value'],myK[3]['value'],convert_to_text(myU[0],"x1"),convert_to_text(myU[1], "x2"),convert_to_text(myU[2], "x3")), 'k':myK, 'utilities':myU}
    elif len(myK)-1==4:
        return {'U':utilite4(myK[0]['value'],myK[1]['value'],myK[2]['value'],myK[3]['value'],myK[4]['value'],convert_to_text(myU[0],"x1"),convert_to_text(myU[1], "x2"),convert_to_text(myU[2], "x3"),convert_to_text(myU[3], "x4")), 'k':myK, 'utilities':myU}
    elif len(myK)-1==5:
        return {'U':utilite5(myK[0]['value'],myK[1]['value'],myK[2]['value'],myK[3]['value'],myK[4]['value'],myK[5]['value'],convert_to_text(myU[0],"x1"),convert_to_text(myU[1], "x2"),convert_to_text(myU[2], "x3"),convert_to_text(myU[3], "x4"),convert_to_text(myU[4], "x5")), 'k':myK, 'utilities':myU}
    elif len(myK)-1==6:
        return {'U':utilite6(myK[0]['value'],myK[1]['value'],myK[2]['value'],myK[3]['value'],myK[4]['value'],myK[5]['value'],myK[6]['value'],convert_to_text(myU[0],"x1"),convert_to_text(myU[1], "x2"),convert_to_text(myU[2], "x3"),convert_to_text(myU[3], "x4"),convert_to_text(myU[4], "x5"),convert_to_text(myU[5], "x6")), 'k':myK, 'utilities':myU}
    
    print(len(myK))
    print(len(myU))
    U=1
    return "Error : nothing was done"

def calculUtilityMultilinear(myK, myU):
    print("utility Multilinear")
    U=1
    return (U)




# ---- 2 -----
def calculk2(k1,k2):
    k = symbols('k')
    solution=solve(k1*k2*k+k1+k2-1,k)
    return float(solution[0])


##def utilite2(k1,k2,k):
##    u1=u1.get()
##    u2=u2.get()
##    U=k*k1*k2*u1*u2+k1*u1+k2*u2
##    return (U)

def utilite3(k1,k2,k,u1,u2):
    U=str(k1)+"*"+u1 + str(k2)+"*"+u2 + str(k*k1*k2)+"*"+u1+"*"+u2
    return (U)

# ---- 3 -----
def calculk3(k1,k2,k3):
    coeff=[k1*k2*k3,k1*k2+k2*k3+k1*k3,k1+k2+k3-1] 
    solution = np.roots(coeff)
    liste=[solution[0],solution[1]]
    
    
    if k1+k2+k3>1:
        k=float(round(liste[0],1))
        return (k)
    else:
        k=float(round(liste[1],1))
        return (k)

def utilite3(k1,k2,k3,k,u1,u2,u3):
    U =str(k1)+"*"+u1+"+"
    U+=str(k2)+"*"+u2+"+"
    U+=str(k3)+"*"+u3+"+"
    U+=str(k*k1*k3)+"*"+u1+"*"+u3+"+"
    U+=str(k*k1*k2)+"*"+u1+"*"+u2+"+"
    U+=str(k*k2*k3)+"*"+u2+"*"+u3+"+"
    U+=str(k**2*k1*k2*k3)+"*"+u1+"*"+u2+"*"+u3
    return (U)
    


# ---- 4 -----
def calculk4(k1,k2,k3,k4):
    k = symbols('k')
    solution=solve(k1*k2*k3*k4*k**3+(k1*k2*k3+k1*k2*k4+k2*k3*k4+k1*k3*k4)*k**2+(k1*k2+k2*k3+k1*k3+k1*k4+k2*k4+k3*k4)*k+k1+k2+k3+k4-1,k)
    print(solution)
    return float(solution[0])


##def utilite4(k1,k2,k3,k4,k):
##    u1=u1.get()
##    u2=u2.get()
##    u3=u3.get()
##    u4=u4.get()
##    U=k**3*k1*k2*k3*k4*u1*u2*u3*u4+k**2*(k1*k2*k3*u1*u2*u3+k1*k2*k4*u1*u2*u4+k2*k3*k4*u2*u3*u4+k1*k3*k4*u1*u3*u4)+k*(k1*k2*u1*u2+k2*k3*u2*u3+k1*k3*u1*u3+k1*k4*u1*u4+k2*k4*u2*u4+k3*k4*u3*u4)+k1*u1+k2*u2+k3*u3+k4*u4
##    return (U)

def utilite4(k1,k2,k3,k4,k,u1,u2,u3, u4):
    U =str(k1)+"*"+u1+"+"
    U+=str(k2)+"*"+u2+"+"
    U+=str(k3)+"*"+u3+"+"
    U+=str(k4)+"*"+u4+"+"
    U+=str(k*k1*k2)+"*"+u1+"*"+u2+"+"
    U+=str(k*k1*k3)+"*"+u1+"*"+u3+"+"
    U+=str(k*k1*k4)+"*"+u1+"*"+u4+"+"
    U+=str(k*k2*k3)+"*"+u2+"*"+u3+"+"
    U+=str(k*k3*k4)+"*"+u3+"*"+u4+"+"
    U+=str(k*k2*k4)+"*"+u2+"*"+u4+"+"
    U+=str(k**2*k1*k2*k3)+"*"+u1+"*"+u2+"*"+u3+"+"
    U+=str(k**2*k1*k2*k4)+"*"+u1+"*"+u2+"*"+u4+"+"
    U+=str(k**2*k1*k3*k4)+"*"+u2+"*"+u3+"*"+u4+"+"
    U+=str(k**2*k2*k3*k4)+"*"+u2+"*"+u3+"*"+u4"+"
    U+=str(k**3*k1*k2*k3*k4)+"*"+u1+"*"+u2+"*"+u3+"*"+u4
    return (U)


# ---- 5 -----
def calculk5(k1,k2,k3,k4,k5):
    k = symbols('k')
    solution=solve(k1*k2*k3*k4*k5*k**4+(k1*k2*k3*k5 + k1*k2*k4*k5 + k2*k3*k4*k5 + k1*k3*k4*k5 + k1*k2*k3*k4)*k**3+(k1*k2*k3 + k1*k2*k4 + k1*k2*k5 + k1*k3*k4 +k1*k3*k5 + k1*k4*k5 + k2*k3*k4 + k2*k3*k5 + k2*k4*k5 + k3*k4*k5)*k**2+ (k2*k3 + k1*k3 + k1*k4 + k2*k4 + k3*k4 + k1*k2 + k1*k5 + k2*k5 + k3*k5 + k4*k5)*k + k1+k2+k3+k4+k5-1, k)
    
    return float(solution[0])


##def utilite5(k1,k2,k3,k4,k5,k):
##    u1=u1.get()
##    u2=u2.get()
##    u3=u3.get()
##    u4=u4.get()
##    u5=u5.get()
##    U= k^4*k1*k2*k3*k4*k5*u1*u2*u3*u4*u5 + k^3(k1*k2*k3*k5*u1*u2*u3*u5 + k1*k2*k4*k5*u1*u2*u4*u5 + k2*k3*k4*k5*u2*u3*u5*u4 + k1*k3*k4*k5*u1*u5*u3*u4 + k1*k2*k3*k4*u1*u2*u3*u4) + k**(k1*k2*k3*u1*u2*u3 + k1*k2*k4*u1*u2*u4 + k1*k2*k5*u1*u2*u5 + k1*k3*k4*u1*u3*u4 +k1*k3*k5*u1*u3*u5 + k1*k4*k5*u1*u4*u5 + k2*k3*k4*u2*u3*u4 + k2*k3*k5*u2*u3*u5 + k2*k4*k5*u2*u4*u5 + k3*k4*k5*u3*u4*u5) + k(k2*k3*u2*u3 + k1*k3*u1*u3 + k1*k4*u4*u4 + k2*k4*u2*u4 + k3*k4*u3*u4 + k1*k2*u1*u2 + k1*k5*u1*u5 + k2*k5*u2*u5 + k3*k5*u3*u5 + k4*k5*u4*u5) + k1*u1 + k2*u2 + k3*u3 + k4*u4 + k5*u5
##    return (U)

def utilite5(k1,k2,k3,k4, k5,k,u1,u2,u3, u4, u5):
    U =str(k1)+"*"+u1+"+"
    U+=str(k2)+"*"+u2+"+"
    U+=str(k3)+"*"+u3+"+"
    U+=str(k4)+"*"+u4+"+"
    U+=str(k5)+"*"+u5+"+"
    U+=str(k*k1*k2)+"*"+u1+"*"+u2+"+"
    U+=str(k*k1*k3)+"*"+u1+"*"+u3+"+"
    U+=str(k*k1*k4)+"*"+u1+"*"+u4+"+"
    U+=str(k*k1*k5)+"*"+u1+"*"+u5+"+"
    U+=str(k*k2*k3)+"*"+u2+"*"+u3+"+"
    U+=str(k*k2*k4)+"*"+u2+"*"+u4+"+"
    U+=str(k*k2*k5)+"*"+u2+"*"+u5+"+"
    U+=str(k*k3*k4)+"*"+u3+"*"+u4+"+"
    U+=str(k*k3*k5)+"*"+u3+"*"+u5+"+"
    U+=str(k*k4*k5)+"*"+u4+"*"+u5+"+"
    U+=str(k**2*k1*k2*k3)+"*"+u1+"*"+u2+"*"+u3+"+"
    U+=str(k**2*k1*k2*k5)+"*"+u1+"*"+u2+"*"+u5+"+"
    U+=str(k**2*k1*k3*k4)+"*"+u1+"*"+u3+"*"+u4+"+"
    U+=str(k**2*k1*k2*k4)+"*"+u1+"*"+u2+"*"+u4+"+"
    U+=str(k**2*k2*k3*k4)+"*"+u2+"*"+u3+"*"+u4+"+"
    U+=str(k**2*k1*k3*k5)+"*"+u1+"*"+u3+"*"+u5+"+"
    U+=str(k**2*k1*k4*k5)+"*"+u1+"*"+u4+"*"+u5+"+"
    U+=str(k**2*k2*k3*k5)+"*"+u2+"*"+u3+"*"+u5+"+"
    U+=str(k**2*k4*k2*k5)+"*"+u4+"*"+u2+"*"+u5+"+"
    U+=str(k**2*k3*k4*k5)+"*"+u3+"*"+u4+"*"+u5+"+"
    U+=str(k**3*k1*k2*k3*k4)+"*"+u1+"*"+u2+"*"+u3+"*"+u4+"+"
    U+=str(k**3*k1*k3*k4*k5)+"*"+u1+"*"+u5+"*"+u3+"*"+u4+"+"
    U+=str(k**3*k1*k2*k3*k5)+"*"+u1+"*"+u2+"*"+u3+"*"+u5+"+"
    U+=str(k**3*k1*k2*k4*k5)+"*"+u1+"*"+u2+"*"+u4+"*"+u5+"+"
    U+=str(k**3*k2*k3*k4*k5)+"*"+u2+"*"+u3+"*"+u4+"*"+u5+"+"
    U+=str(k**4*k1*k2*k3*k4*k5)+"*"+u1+"*"+u2+"*"+u3+"*"+u4+"*"+u5
    return (U)



# ---- 6 -----
def calculk6(k1,k2,k3,k4,k5,k6):
    k = symbols('k')
    a=k1*k2*k3*k4*k5*k6
    b=(k1*k2*k3*k5*k6 + k1*k2*k3*k4*k5 + k1*k2*k4*k5*k6 + k2*k3*k4*k5*k6 + k1*k3*k4*k5*k6 + k1*k2*k3*k4*k6)
    c=(k1*k2*k3*k5 + k1*k2*k4*k5 + k2*k3*k4*k5 + k1*k3*k4*k5 + k1*k2*k3*k4 + k1*k2*k3*k6 + k1*k2*k4*k6 + k1*k2*k5*k6 + k1*k3*k4*k6 + k1*k3*k5*k6 + k1*k4*k5*k6 + k2*k3*k4*k6 + k2*k3*k5*k6  + k2*k4*k5*k6 + k3*k4*k5*k6)
    d=(k1*k2*k3 + k1*k2*k4 + k1*k2*k5 + k1*k3*k4 +k1*k3*k5 + k1*k4*k5 + k2*k3*k4 + k2*k3*k5 + k2*k4*k5 + k3*k4*k5 + k3*k4*k6 + k1*k2*k6 + k1*k3*k6 + k1*k4*k6 + k1*k5*k6 + k3*k4*k6 + k3*k5*k6 + k2*k4*k6 + k2*k5*k6 + k4*k5*k6)
    e=(k2*k3 + k1*k3 + k1*k4 + k1*k6 + k1*k5 + k1*k2 + k2*k4 + k3*k4 + k2*k5 + k3*k5 + k4*k5 + k2*k6 + k3*k6 + k4*k6 + k5*k6)
    f= k1+k2+k3+k4+k5+k6-1
    p_k=lambda k: a*k**5+b*k**4+c*k**3+d*k**2+e*k+f
    
    solutions=fsolve(p_k, 0, xtol=1.49012e-08, maxfev=100000000)
    return float(solutions[0])


##def utilite6(k1,k2,k3,k4,k):
##    	u1=u1.get()
##    	u2=u2.get()
##    	u3=u3.get()
##	u4=u4.get()
##	u5=u5.get()
##	u6=u6.get()
##   	U= k**5*k1*k2*k3*k4*k5*k6 + k**4(k1*k2*k3*k5*k6*u1*u2*u3*u5*u6 + k1*k2*k3*k4*k5*u1*u2*u3*u4*u5 + k1*k2*k4*k5*k6*u1*u2*u4*u5*u6 + k2*k3*k4*k5*k6*u2*u3*u4*u5*u6 + k1*k3*k4*k5*k6*u1*u3*u4*u5*u6 + k1*k2*k3*k4*k6*u1*u2*u3*u4*u6) +  k^3(k1*k2*k3*k5*u1*u2*u3*u5 + k1*k2*k4*k5*u1*u2*u4*u5 + k2*k3*k4*k5*u2*u3*u4*u5 + k1*k3*k4*k5*u1*u3*u4*u5 + k1*k2*k3*k4*u1*u2*u3*u4 + k1*k2*k3*k6*u1*u2*u3*u6 + k1*k2*k4*k6*u1*u2*u4*u6 + k1*k2*k5*k6*u1*u2*u5*u6 + k1*k3*k4*k6*u1*u3*u4*u6 + k1*k3*k5*k6*u1*u3*u5*u6 + k1*k4*k5*k6*u1*u4*u5*u6 + k2*k3*k4*k6*u2*u3*u4*u6 + k2*k3*k5*k6*u2*u3*u5*u6  + k2*k4*k5*k6*u2*u4*u5*u6 + k3*k4*k5*k6*u3*u4*u5*u6) + k**(k1*k2*k3*u1*u2*u3 + k1*k2*k4*u1*u2*u4 + k1*k2*k5*u1*u2*u5 + k1*k3*k4*u1*u3*u4 +k1*k3*k5*u1*u3*u5 + k1*k4*k5*u1*u4*u5 + k2*k3*k4*u2*u3*u4 + k2*k3*k5*u2*u3*u5 + k2*k4*k5*u2*u4*u5 + k3*k4*k5*u3*u4*u5 + k3*k4*k6*u3*u4*u6 + k1*k2*k6*u1*u2*u6 + k1*k3*k6*u1*u3*u6 + k1*k4*k6*u1*u4*u6 + k1*k5*k6*u1*u5*u6 + k3*k4*k6*u3*u4*u6 + k3*k5*k6*u3*u5*u6 + k2*k4*k6*u2*u4*u6 + k2*k5*k6*u2*u5*u6 + k4*k5*k6*u4*u5*u6) + k*(k2*k3*u2*u3 + k1*k3*u1*u3 + k1*k4*u1*u4 + k1*k6*u1*u6 + k1*k5*u1*u5 + k1*k2*u1*u2 + k2*k4*u2*u4 + k3*k4*u3*u4 + k2*k5*u2*u5 + k3*k5*u3*u5 + k4*k5*u4*u5 + k2*k6*u2*u6 + k3*k6*u3*u6 + k4*k6*u4*u6 + k5*k6*u5*u6) + k1*u1 +k2*u2 +k3*u3 +k4*u4 +k5*u5 +k6*u6
##
##	return (U)
def utilite5(k1,k2,k3,k4, k5,k,u1,u2,u3, u4, u5):

    U =str(k1)+"*"+u1+"+"
    U+=str(k2)+"*"+u2+"+"
    U+=str(k3)+"*"+u3+"+"
    U+=str(k4)+"*"+u4+"+"
    U+=str(k5)+"*"+u5+"+"
    U+=str(k6)+"*"+u6+"+"
    U+=str(k*k1*k2)+"*"+u1+"*"+u2+"+"
    U+=str(k*k1*k3)+"*"+u1+"*"+u3+"+"
    U+=str(k*k1*k4)+"*"+u1+"*"+u4+"+"
    U+=str(k*k1*k5)+"*"+u1+"*"+u5+"+"
    U+=str(k*k1*k6)+"*"+u1+"*"+u6+"+"
    U+=str(k*k2*k3)+"*"+u2+"*"+u3+"+"
    U+=str(k*k2*k4)+"*"+u2+"*"+u4+"+"
    U+=str(k*k2*k5)+"*"+u2+"*"+u5+"+"
    U+=str(k*k2*k6)+"*"+u2+"*"+u6+"+"
    U+=str(k*k3*k4)+"*"+u3+"*"+u4+"+"
    U+=str(k*k3*k5)+"*"+u3+"*"+u5+"+"
    U+=str(k*k3*k6)+"*"+u3+"*"+u6+"+"
    U+=str(k*k4*k5)+"*"+u4+"*"+u5+"+"
    U+=str(k*k4*k6)+"*"+u4+"*"+u6+"+"
    U+=str(k*k5*k6)+"*"+u5+"*"+u6+"+"
    U+=str(k**2*k1*k2*k3)+"*"+u1+"*"+u2+"*"+u3+"+"
    U+=str(k**2*k1*k2*k5)+"*"+u1+"*"+u2+"*"+u5+"+"
    U+=str(k**2*k1*k3*k4)+"*"+u1+"*"+u3+"*"+u4+"+"
    U+=str(k**2*k1*k2*k4)+"*"+u1+"*"+u2+"*"+u4+"+"
    U+=str(k**2*k2*k3*k4)+"*"+u2+"*"+u3+"*"+u4+"+"
    U+=str(k**2*k1*k3*k5)+"*"+u1+"*"+u3+"*"+u5+"+"
    U+=str(k**2*k1*k4*k5)+"*"+u1+"*"+u4+"*"+u5+"+"
    U+=str(k**2*k2*k3*k5)+"*"+u2+"*"+u3+"*"+u5+"+"
    U+=str(k**2*k4*k2*k5)+"*"+u4+"*"+u2+"*"+u5+"+"
    U+=str(k**2*k3*k4*k5)+"*"+u3+"*"+u4+"*"+u5+"+"
    U+=str(k**2*k1*k2*k6)+"*"+u1+"*"+u2+"*"+u6+"+"
    U+=str(k**2*k1*k3*k6)+"*"+u1+"*"+u3+"*"+u6+"+"
    U+=str(k**2*k1*k4*k6)+"*"+u1+"*"+u4+"*"+u6+"+"
    U+=str(k**2*k1*k5*k6)+"*"+u1+"*"+u5+"*"+u6+"+"
    U+=str(k**2*k2*k3*k6)+"*"+u2+"*"+u3+"*"+u6+"+"
    U+=str(k**2*k2*k4*k6)+"*"+u2+"*"+u4+"*"+u6+"+"
    U+=str(k**2*k2*k5*k6)+"*"+u2+"*"+u5+"*"+u6+"+"
    U+=str(k**2*k3*k4*k6)+"*"+u3+"*"+u4+"*"+u6+"+"
    U+=str(k**2*k3*k5*k6)+"*"+u3+"*"+u5+"*"+u6+"+"
    U+=str(k**2*k4*k5*k6)+"*"+u4+"*"+u5+"*"+u6+"+" 
    U+=str(k**3*k1*k2*k3*k4)+"*"+u1+"*"+u2+"*"+u3+"*"+u4+"+"
    U+=str(k**3*k1*k3*k4*k5)+"*"+u1+"*"+u5+"*"+u3+"*"+u4+"+"
    U+=str(k**3*k1*k2*k3*k5)+"*"+u1+"*"+u2+"*"+u3+"*"+u5+"+"
    U+=str(k**3*k1*k2*k4*k5)+"*"+u1+"*"+u2+"*"+u4+"*"+u5+"+"
    U+=str(k**3*k2*k3*k4*k5)+"*"+u2+"*"+u3+"*"+u4+"*"+u5+"+"
    U+=str(k**3*k1*k2*k3*k6)+"*"+u1+"*"+u2+"*"+u3+"*"+u6+"+"
    U+=str(k**3*k1*k2*k4*k6)+"*"+u1+"*"+u2+"*"+u4+"*"+u6+"+"
    U+=str(k**3*k1*k2*k5*k6)+"*"+u1+"*"+u2+"*"+u5+"*"+u6+"+"
    U+=str(k**3*k1*k3*k5*k6)+"*"+u1+"*"+u3+"*"+u5+"*"+u6+"+"
    U+=str(k**3*k1*k4*k5*k6)+"*"+u1+"*"+u4+"*"+u5+"*"+u6+"+"
    U+=str(k**3*k2*k3*k4*k6)+"*"+u2+"*"+u3+"*"+u4+"*"+u6+"+"
    U+=str(k**3*k1*k3*k4*k6)+"*"+u1+"*"+u3+"*"+u4+"*"+u6+"+"
    U+=str(k**3*k2*k3*k5*k6)+"*"+u2+"*"+u3+"*"+u5+"*"+u6+"+"
    U+=str(k**3*k2*k4*k5*k6)+"*"+u2+"*"+u4+"*"+u5+"*"+u6+"+"
    U+=str(k**3*k1*k2*k5*k6)+"*"+u1+"*"+u2+"*"+u5+"*"+u6+"+"
    U+=str(k**4*k1*k2*k3*k4*k5)+"*"+u1+"*"+u2+"*"+u3+"*"+u4+"+"+u5+"+"
    U+=str(k**4*k1*k2*k3*k4*k6)+"*"+u1+"*"+u2+"*"+u3+"*"+u4+"+"+u6+"+"
    U+=str(k**4*k1*k2*k3*k5*k6)+"*"+u1+"*"+u2+"*"+u3+"*"+u5+"+"+u6+"+"
    U+=str(k**4*k1*k2*k4*k5*k6)+"*"+u1+"*"+u2+"*"+u4+"*"+u5+"+"+u6+"+"
    U+=str(k**4*k1*k3*k4*k5*k6)+"*"+u1+"*"+u3+"*"+u4+"*"+u5+"+"+u6+"+"
    U+=str(k**4*k2*k3*k4*k5*k6)+"*"+u2+"*"+u3+"*"+u4+"*"+u5+"+"+u6+"+"
    U+=str(k**5*k1*k2*k3*k4*k5*k6)+"*"+u1+"*"+u2+"*"+u3+"*"+u4+"*"+u5+"+"+u6


def reduce(nombre):
    return math.floor(nombre*100000000.0)/100000000.0;

def signe(nombre):
    if nombre>=0:
        return "+"+str(nombre)
    else:
        return str(nombre)


def convert_to_text(data, x):
    print("convert")
    print(json.dumps(data))
    if data['type']=="exp":
        return "("+str(reduce(data['a']))+"*exp("+signe(-reduce(data['b']))+x+")"+signe(reduce(data['c']))+")";
    elif data['type']=="log":
        return "("+str(reduce(data['a']))+"*log("+str(reduce(data['b']))+x+signe(reduce(data['c']))+")"+signe(reduce(data['d']))+")";
    elif data['type']=="pow":
        return "("+str(reduce(data['a']))+"*(pow("+x+","+str(reduce(1-data['b']))+")-1)/("+str(reduce(1-data['b']))+")"+signe(reduce(data['c']))+")";
    elif data['type']=="quad":
        return "("+str(reduce(data['c']))+"*"+x+signe(reduce(-data['b']))+"*pow("+x+",2)"+signe(reduce(data['a']))+")";
    elif data['type']=="lin":
        return "("+str(reduce(data['a']))+"*"+x+signe(reduce(data['b']))+")";




