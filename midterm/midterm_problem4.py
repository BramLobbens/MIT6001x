# MIT 6.00.1x Midterm Problem 4

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    exp = 0
    while base**exp < num:
        exp += 1
        if base**exp >= num:
            break
    if abs(base**exp - num) >= abs(base**(exp-1) - num):
        exp -= 1
    
    return exp