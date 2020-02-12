def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
       return 1.0
    else:
       return base * iterPower(base, exp-1)
