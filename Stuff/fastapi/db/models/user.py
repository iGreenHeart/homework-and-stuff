from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: Optional[str] = Field(default=None)
    username: str
    email: str
