from enum import Enum

from pydantic import BaseModel, Field


class TodoPriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class TodoRequest(BaseModel):
    title: str = Field(description="Todo Title", min_length=3, max_length=100)
    description: str = Field(description="More info", min_length=3, max_length=100)
    priority: str = Field(description="Priority", default=TodoPriority.LOW)
    completed: bool = Field(default=False)
    is_public: bool = Field(default=True)


class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    priority: str
    completed: bool
    is_public: bool
    owner_id: int
