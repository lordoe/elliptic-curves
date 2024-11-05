def multiplicative_inverse(a: int, p: int) -> int:
    """
    Compute the multiplicative inverse of a modulo p.
    
    Parameters:
        a (int): The number to invert.
        p (int): The modulus.
    
    Returns:
        int: The multiplicative inverse of a modulo p.
    
    Raises:
        ValueError: If the inverse does not exist.
    """
    try:
        return pow(a, -1, p)
    except ValueError:
        raise ValueError(f'{a} has no inverse modulo {p}')
