from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.service.just_ai_service import JustAiService

router = APIRouter()

# Modelo de dados para entrada do usuário
class UserRequest(BaseModel):
    name: str
    age: int
    city: str
    problem_summary: str

# Rota para processar a solicitação do usuário
@router.post("/legal-advice")
def get_legal_advice(user_request: UserRequest):
    
    try:
        advice = generate_legal_advice(
            user_request.name,
            user_request.age,
            user_request.city,
            user_request.problem_summary
        )
        return {"advice": advice}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Função para gerar resposta usando OpenAI
def generate_legal_advice(name: str, age: int, city: str, problem_summary: str) -> str:
    prompt = f"""
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
    
    response = client.completions.create(engine="gpt-4o",
    prompt=prompt,
    max_tokens=500)
    
    return response.choices[0].text.strip()
