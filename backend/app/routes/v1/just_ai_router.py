import logging
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.service.just_ai_service import JustAiService
from app.models.user_request_model import UserRequest

router = APIRouter()
# logger = logging.getLogger(__name__)

# Rota para processar a solicitação do usuário
@router.post("/legal-advice")
def get_legal_advice(request: UserRequest):

    # logger.info(f"[{__name__}] - Received request: {request}")
    
    justAiService = JustAiService()
    response = justAiService.execute(request)
    
    # logger.info(
    # f"[{__name__}] - Generate response:response={response}")


    return {"response": response}
    