from pydantic import BaseModel

# Modelo de dados para entrada do usuário
class UserRequest(BaseModel):
    name: str
    age: int
    city: str
    problem_summary: str