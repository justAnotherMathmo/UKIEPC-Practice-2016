import sys

from math import log

def binary_search(func, x_min, x_max, tol=10**(-15), itera=None):
    """Finds an approximate root to func within the range x_min to x_max via a binary search
    If itera is not None, will limit to itera iterations, as well as tolerance"""
    l_sign, r_sign = 2*(func(x_min) > 0) - 1, 2*(func(x_max) > 0) -1
    if l_sign == r_sign:
        raise ValueError("func(x_min) and func(x_max) must have opposite signs")
    x_new = x_max
    while abs(func(x_max)) > tol:
        x_new = (x_min + x_max)/2
        n_sign = 2*(func(x_new) > 0) - 1
        if n_sign == l_sign:
            x_min = x_new
        else:
            x_max = x_new
    return x_new

def appx_k(k):
    return log((n+k)/(n+k-p)) - 1/k - p/(2*(n+k)*(n+k-p))

def prob_funct(k): 
    res = p*k/(n+k - (p-1))
    for r in range(p-1):
        res *= (n-r)/(n+k-r)
    return res

lines = []
for line in sys.stdin:
    n, p = map(int, line.split(' '))

try:
    k_apx = binary_search(appx_k, 1, n**2)
    k_tries = [k for k in range(max(1, int(k_apx)-2), int(k_apx)+3)]+[1]
except ValueError:
    k_tries = [1]

print(max(prob_funct(k) for k in k_tries))
