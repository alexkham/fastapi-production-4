import math
from fastapi import HTTPException

def permutation_full(n: int) -> int:
    return math.factorial(n)

def permutation_identical(n: int, groups: list[int]) -> int:
    denom = 1
    for count in groups:
        denom *= math.factorial(count)
    return math.factorial(n) // denom

def permutation_partial(n: int, r: int) -> int:
    if r > n:
        raise HTTPException(status_code=400, detail="r must be ≤ n")
    return math.factorial(n) // math.factorial(n - r)

def permutation_with_repetition(n: int, r: int) -> int:
    return n ** r

def circular_permutation(n: int) -> int:
    if n <= 0:
        raise HTTPException(status_code=400, detail="n must be > 0")
    return math.factorial(n - 1)

def combination(n: int, r: int) -> int:
    if r > n:
        raise HTTPException(status_code=400, detail="r must be ≤ n")
    return math.comb(n, r)

def partition_into_groups(n: int, group_sizes: list[int]) -> int:
    if sum(group_sizes) != n:
        raise HTTPException(status_code=400, detail="Sum of group sizes must equal n")
    denom = 1
    for size in group_sizes:
        denom *= math.factorial(size)
    return math.factorial(n) // denom

def weak_composition(n: int, r: int) -> int:
    return math.comb(n + r - 1, r - 1)

def strong_composition(n: int, r: int) -> int:
    if n < r:
        raise HTTPException(status_code=400, detail="n must be ≥ r")
    return math.comb(n - 1, r - 1)

def distribution_into_cells(n: int, r: int) -> int:
    return r ** n
