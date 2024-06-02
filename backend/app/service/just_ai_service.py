import logging
from app.handler.openai_handler import OpenAiHandler
from app.models.user_request_model import UserRequest

class JustAiService: 
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.openai_handler = OpenAiHandler()

    def execute(self, data: UserRequest):
        self.logger.debug(f"[{__name__}] - Executing ...")
        
        (name, age, city, problem_summary) = (data.name, data.age, data.city, data.problem_summary)
        message = f"""
            Você é um assistente jurídico. Um cliente chamado {name}, com {age} anos, da cidade de {city} descreveu o seguinte problema:
            "{problem_summary}"
            
            Forneça uma orientação detalhada sobre como resolver esse problema na cidade de {city}, incluindo:
            - Passos específicos para resolver o problema
            - Sugestões de documentos necessários
            - Endereço do departamento da cidade relevante
            - Recomendação para ligar antes de visitar, se aplicável
            - Detalhes personalizados de acordo com a idade do cliente para garantir clareza

            Responda de forma clara e detalhada, adequada para a idade de {age} anos.
        """
        
        response = self.openai_handler.execute_with_gpt4(message)
        
        self.logger.debug(f"[{__name__}] - Finished")

        return response