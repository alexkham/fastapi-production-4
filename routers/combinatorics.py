from fastapi import APIRouter
from models.combinatorics import (
    NOnly,
    NandR,
    IdenticalPermutationInput,
    PartitionGroupsInput,
)
from services.combinatorics_ops import *
from fastapi import Body

router = APIRouter(prefix='/combinatorics',
    tags=['combinatorics']
)

@router.post("/permutation-full")
def route_permutation_full(data: NOnly):
    return {"result": permutation_full(data.n)}

@router.post("/permutation-identical")
def route_permutation_identical(data: IdenticalPermutationInput):
    return {"result": permutation_identical(data.n, data.groups)}

@router.post("/permutation-partial")
def route_permutation_partial(data: NandR):
    return {"result": permutation_partial(data.n, data.r)}

@router.post("/permutation-with-repetition")
def route_permutation_with_repetition(data: NandR):
    return {"result": permutation_with_repetition(data.n, data.r)}

@router.post("/permutation-circular")
def route_circular_permutation(data: NOnly):
    return {"result": circular_permutation(data.n)}

@router.post("/combination")
def route_combination(data: NandR):
    return {"result": combination(data.n, data.r)}

@router.post("/partition-into-groups")
def route_partition_into_groups(data: PartitionGroupsInput):
    return {"result": partition_into_groups(data.n, data.group_sizes)}

@router.post("/composition-weak")
def route_weak_composition(data: NandR):
    return {"result": weak_composition(data.n, data.r)}

@router.post("/composition-strong")
def route_strong_composition(data: NandR):
    return {"result": strong_composition(data.n, data.r)}

@router.post("/distribution-into-cells")
def route_distribution_into_cells(data: NandR):
    return {"result": distribution_into_cells(data.n, data.r)}
