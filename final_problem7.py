# MIT 6.00.1x Final Exam Problem 7

from functools import reduce

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """

    def apply_value(x):
        g = lambda y, z: y + z
        for i, e in enumerate(L):
            L[i] = e * (x**(len(L) - (i+1)))
        return reduce(g, L)
    
    return apply_value

a = general_poly([1, 2, 3, 4])(10)
print(a)