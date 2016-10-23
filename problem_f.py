import sys

from math import log

def newton_rhapson(func, func_d, x0, tol=10**(-9), itera=None):
    """Uses the Newton Rhapson method to find an approximate root to func near x0.
    func_d is the derivative of func.
    If itera is not None, will limit to itera iterations, as well as tolerance"""
    res = x0
    loops = 0
    while True:
        res = res - func(res)/func_d(res)
        loops += 1
        if abs(func(res)) < tol or (itera is not None and loops >= itera):
            break
    return res

def appx_k(k):
    return log((n+k)/(n+k-p)) - 1/k - p/(2*(n+k)*(n+k-p))

def appx_k_d(k):
    return 1/k**2 - p*(2*k**2+2*n**2+p-2*n*(1+p)+k*(4*n-2*(1+p))) / (2*(k+n)**2*(k+n-p)**2)

lines = []
for line in sys.stdin:
    n, p = map(int, line.split(' '))

k_apx = newton_rhapson(appx_k, appx_k_d, p/2, tol=10**(-2))
k_tries = [k for k in range(max(1, int(k_apx)-2), int(k_apx)+3)]+[1]

def prob_funct(k): 
    res = p*k/(n+k - (p-1))
    for r in range(p-1):
        res *= (n-r)/(n+k-r)
    return res

print(max(prob_funct(k) for k in k_tries))
