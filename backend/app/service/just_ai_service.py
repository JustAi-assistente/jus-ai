import logging
from app.handler.openai_handler import OpenAiHandler

class JustAiService: 
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.openai_handler = OpenAiHandler()

    def execute(self, data):
        self.logger.debug(f"[{__name__}] - Executing ...")
        
        s3_system_template_name = 'summarizer_system_prompt.txt'
        s3_template_name = 'summarizer_prompt.txt'
        
        response = self.openai_handler.execute_with_gpt4(data, s3_system_template_name, s3_template_name)
        
        self.logger.debug(f"[{__name__}] - Finished")

        return response