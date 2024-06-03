import logging
from app.models.schema import SystemMessage, BaseMessage, HumanMessage
from typing import List
from app.models.schema import convert_message_to_dict
class GptBuilder:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def build_gpt_object_array(self, messages: List[BaseMessage], prompt):
        self.logger.info(f"[{__name__}] - Building GPT object array...")
        
        openai_message_object_array = []
        openai_message_object_array.append(convert_message_to_dict(SystemMessage(content=prompt)))
        
        for message in messages:
            if message.role == "user":
                message = HumanMessage(content=message.content)
            elif message.role == "system":
                message = SystemMessage(content=message.content)
            openai_message_object_array.append(convert_message_to_dict(message))
            
        self.logger.info(f"[{__name__}] - GPT object array: {openai_message_object_array}")
        return openai_message_object_array