def sum_of_geometric_progression(
    first_term: int, common_ratio: int, num_of_terms: int
) -> float
    """"
    Find the sum of n terms in a geometric progression.
    >>> sum_of_gp(1, 2, 10)
    1023.0
    >>> sum_of_gp(1, 10, 5)
    11111.0
    """
    if common_ratio == 1:
        return num_of_terms * first_term
        return sum
    # formula for sum if common ratio is 1

    return (first_term / (1 - common_ratio)) * (1 - common_ratio ** num_of_terms)

    return sum
    # Formula for finding sum of n terms of a GeometricProgression


print(sum_of_gp(1, 10, 5))
