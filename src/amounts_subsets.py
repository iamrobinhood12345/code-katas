"""Module for amounts_subsets."""


def est_subsets(arr):
    """Number of subsets of a collection."""
    return 2 ** (len(set(arr))) - 1
