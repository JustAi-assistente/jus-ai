import logging
from app.ai_models.ai_models import AIModels

class OpenAiHandler:

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.api_models = AIModels()
        
    def execute_with_gpt4(self, message) -> str:
        self.logger.info(f"[{__name__}] - executing ...")

        try:
            output_text = self.api_models.run_gpt4(message)

            self.logger.info(f"[{__name__}] - output_text: {output_text}")
            return output_text
        except Exception as e:
            self.logger.error(
                f"[{__name__}] - Error while running openai with message: {e}")
            raise e

        self.logger.debug(f"[{__name__}] - executig ...")

        system_template = self.template.get_template_message_from_s3(s3_system_template_name)
        template = self.template.get_template_message_from_s3(s3_template_name)

        openai_message_object_array = self.gpt_builder.build_gpt_object_array(
        context, system_template, template)

        try:
            output_text = self.api_models.run_gpt35(openai_message_object_array)

            self.logger.info(f"[{__name__}] - output_text: {output_text}")
            return output_text
        except Exception as e:
            self.logger.error(
                f"[{__name__}] - Error while running openai with message: {e}")
            raise e