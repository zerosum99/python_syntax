class Foo():
    """
    >>> 3+2
    5
    """
    pass

if __name__ in ("__main__", "__console__"):
    import doctest
    doctest.testmod(verbose=True)