class MyClass(object):
    pass

def unpredictable(obj):
    """Returns a new list containing obj.

    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<__main__.MyClass object at 0x...>]
    """
    return [obj]

if __name__ in ("__main__", "__console__"):
    import doctest
    doctest.testmod(verbose=True)