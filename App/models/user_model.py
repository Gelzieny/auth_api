from pydantic import BaseModel, EmailStr

class UserModel(BaseModel):
    nome: str
    sobrenome: str
    username: str
    password: str
    email: EmailStr 