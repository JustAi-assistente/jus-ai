import logging
from typing import List
from app.ai_models.ai_models import AIModels
from app.templates.custom_template import CustomTemplate
from app.builder.gpt_builder import GptBuilder
from app.models.schema import BaseMessage
class OpenAiHandler:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.api_models = AIModels()
        self.template = CustomTemplate()
        self.gpt_builder = GptBuilder()
        
    def execute_with_gpt4(self, messages: List[BaseMessage]) -> str:
        self.logger.info(f"[{__name__}] - executing ...")

        system_prompt = self.template.get_system_template()
        openai_message_object_array = self.gpt_builder.build_gpt_object_array(messages, system_prompt)
        
        try:
            output_text = self.api_models.run_gpt4(openai_message_object_array)

            self.logger.info(f"[{__name__}] - output_text: {output_text}")
            return output_text
        except Exception as e:
            self.logger.error(
                f"[{__name__}] - Error while running openai with message: {e}")
            raise e