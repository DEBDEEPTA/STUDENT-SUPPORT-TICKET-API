from pydantic import BaseModel,Field
from typing import Optional
class User(BaseModel):
    user_id : Optional[str] = None
    user_name : Optional[str] = None
    email : str
    password : str

class UserLogin(BaseModel):
    email: str
    password: str
