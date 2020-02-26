def silnia(x):
    '''
    Input: int > 0
    Output: factorial of the given int
    '''
    if x == 1:
        return 1
    else:
        return x * silnia(x - 1)
