import logging
from app.handler.openai_handler import OpenAiHandler
from app.models.user_request_model import UserRequest

class JustAiService: 
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.openai_handler = OpenAiHandler()

    def execute(self, data: UserRequest):
        self.logger.debug(f"[{__name__}] - Executing ...")
        
        response = self.openai_handler.execute_with_gpt35(data.messages)
        
        self.logger.debug(f"[{__name__}] - Finished")

        return response