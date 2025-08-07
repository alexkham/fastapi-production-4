from pydantic import BaseModel, Field
from typing import List

class NOnly(BaseModel):
    n: int = Field(..., ge=0)

class NandR(BaseModel):
    n: int = Field(..., ge=0)
    r: int = Field(..., ge=0)

class IdenticalPermutationInput(BaseModel):
    n: int = Field(..., ge=0)
    groups: List[int]

class PartitionGroupsInput(BaseModel):
    n: int = Field(..., ge=0)
    group_sizes: List[int]
