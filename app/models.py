from pydantic import BaseModel, Field
from datetime import datetime
from typing import List
import uuid

# Constants
MAX_TITLE_LENGTH = 200
MAX_INGREDIENTS = 50

# Recipe schema (Jamie's requirements):
# - instructions: array of separate step strings (not a single text block)
# - cuisine: dedicated cuisine/region string field
# - difficulty: removed (subjective and unhelpful)

class Recipe(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str 
    description: str
    ingredients: List[str]
    instructions: List[str]
    tags: List[str] = Field(default_factory=list)
    cuisine: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class RecipeCreate(BaseModel):
    title: str
    description: str
    ingredients: List[str]
    instructions: List[str]
    tags: List[str] = Field(default_factory=list)
    cuisine: str


class RecipeUpdate(BaseModel):
    title: str
    description: str
    ingredients: List[str]
    instructions: List[str]
    tags: List[str]
    cuisine: str
