def pow(base, exponent):
    """Replicate c++ pow function in python
       return base ** exponent
    """
    if type(base) is not float:
        raise TypeError("Base must be a float!")
    return base ** exponent

