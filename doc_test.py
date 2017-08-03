'''
>>> print(list(range(20)))  # doctest:  +ELLIPSIS
[0, 1, ..., 18, 19]
>>> print(list(range(20))) # doctest: +NORMALIZE_WHITESPACE
[0,   1,  2,  3,  4,  5,  6,  7,  8,  9,
10,  11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> print(list(range(20))) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
[0,    1, ...,   18,    19]
>>> print(list(range(20))) # doctest: +ELLIPSIS
...                 # doctest: +NORMALIZE_WHITESPACE
[0,    1, ...,   18,    19]
'''


if __name__ in ("__main__", "__console__"):
    import doctest
    doctest.testmod(verbose=True)