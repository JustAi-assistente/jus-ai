from typing import List
from pydantic import BaseModel, Field
from abc import abstractmethod

class BaseMessage(BaseModel):
    """Message object."""

    content: str
    additional_kwargs: dict = Field(default_factory=dict)

    @property
    @abstractmethod
    def type(self) -> str:
        """Type of the message, used for serialization."""

class SystemMessage(BaseMessage):
    """Type of message that is a system message."""

    @property
    def type(self) -> str:
        """Type of the message, used for serialization."""
        return "system"

class HumanMessage(BaseMessage):
    """Type of message that is spoken by the human."""

    @property
    def type(self) -> str:
        """Type of the message, used for serialization."""
        return "human"


def convert_array_message_to_dict(messages: List[BaseMessage]) -> List[dict]:
    return [convert_message_to_dict(m) for m in messages]

def convert_message_to_dict(message: BaseMessage) -> dict:
    if isinstance(message, HumanMessage):
        message_dict = {"role": "user", "content": message.content}
    elif isinstance(message, SystemMessage):
        message_dict = {"role": "system", "content": message.content}
    else:
        raise ValueError(f"Got unknown type {message}")
    if "name" in message.additional_kwargs:
        message_dict["name"] = message.additional_kwargs["name"]
    return message_dict