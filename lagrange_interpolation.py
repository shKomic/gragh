import numpy as np

def lagurange(x,xp,fx):
    results = [];
    for l in range(len(x)):
        if(x[l] in xp):
            results.append(fx[np.where(xp==x[l])])
        else:
            result=0
            for j in range(len(xp)):
                lag = lx(x[l],j,xp)
                result += fx[j]*lag
            results.append(result)
    return results

def lx(x,j,xp):
    numerator,denominator = 1,1
    for i in range(len(xp)):
        if(i!=j):
            numerator *= x-xp[i]
            denominator *= xp[j]-xp[i]
    return numerator/denominator



