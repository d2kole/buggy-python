"""
The purpose of this snippet is to test your knowledge of
default arguments for functions in python and how they
can be misused
"""
def foo(bar=None):
    """
    Always return a fresh list containing \"baz\" unless a caller provides an
    explicit list. Avoid mutable defaults so repeated calls stay independent.
    """
    if bar is None:
        bar = []
    bar.append("baz")
    return bar
