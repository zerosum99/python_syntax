'''
>>> double_space1.double_space(['Line one.', 'Line two.'])
Line one.
<BLANKLINE>
Line two.
<BLANKLINE>
>>>
'''

def double_space(lines):
    '''Prints a list of lines double-spaced.

    >>> double_space1.double_space(['Line one.', 'Line two.'])
    Line one.
    <BLANKLINE>
    Line two.
    <BLANKLINE>
    >>>
    '''
    for l in lines:
        print(l)
        print()
    return