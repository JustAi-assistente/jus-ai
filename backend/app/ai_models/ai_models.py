import os
import logging
from typing import List
import openai
from openai import OpenAI

from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)
import tenacity  # for exponential backoff

class AIModels:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.client = OpenAI(
            api_key=os.environ["OPENAI_API_KEY"],
    )

    def run_gpt4(self, message, temperature = 1.0):
        model_name = 'gpt-4o'
        self.logger.info(f"[{__name__}] -  Run openai {model_name}...")
        try:
            openai_response = self.__run_gpt(message, model_name, temperature)
            
            self.logger.info(
                f"[{__name__}] - Prompt execute with message: {openai_response}")
            return openai_response
        except tenacity.RetryError as retry_err:
            self.logger.error(
                f"[{__name__}] - Error while running openai with message: {retry_err}")
            raise Exception
        
    @retry(wait=wait_random_exponential(min=60, max=240), stop=stop_after_attempt(3))
    def __run_gpt(self, message, model_name, temperature):        
        self.logger.info(f"[{__name__}] - Run openai gpt with model: {model_name}...")
        try:
            openai_output_text = self.client.chat.completions.create(model=model_name,
             top_p=0,
            temperature = temperature,
            messages=message)

            return openai_output_text.choices[0].message.content
        except Exception as e:
            self.logger.error(f"[{__name__}] - Error getting into OPENAI= {e}")
            raise e
        
