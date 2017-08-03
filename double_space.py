
def double_space(lines):
    '''Prints a list of lines double-spaced.

    >>> double_space.double_space(['Line one.', 'Line two.'])
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

if __name__ in ("__main__", "__console__"):
    import doctest
    doctest.testmod(verbose=True)