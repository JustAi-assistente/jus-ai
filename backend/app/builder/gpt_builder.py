import logging

class GptBuilder:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def build_gpt_object_array(self, messages, prompt):
        self.logger.info(f"[{__name__}] - Building GPT object array...")
        
        openai_message_object_array = []
        openai_message_object_array.append(prompt)
        openai_message_object_array.append(messages)
        
        self.logger.info(f"[{__name__}] - GPT object array: {openai_message_object_array}")
        return openai_message_object_array