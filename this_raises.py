def this_raises():
    '''This function always raises an exception.

    >>> this_raises()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/no/such/path/doctest_tracebacks.py", line 14, in this_raises
        raise RuntimeError('here is the error')
    RuntimeError: here is the error
    '''
    raise RuntimeError('here is the error')
    
if __name__ in ("__main__", "__console__"):
    import doctest
    doctest.testmod(verbose=True)