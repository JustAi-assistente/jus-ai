from pydantic import BaseModel
from typing import List
class OpenaiMessage(BaseModel):
    role: str
    content: str
class UserRequest(BaseModel):
    messages: List[OpenaiMessage]