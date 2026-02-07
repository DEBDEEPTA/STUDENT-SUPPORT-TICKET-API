from fastapi import APIRouter, HTTPException
from schemas.user import UserLogin
from in_memory_db.in_memory_users.users import get_users, get_admins
from utils.jwt_handaler import create_token
from utils.logger import logger
router = APIRouter()

# LOGIN HANDLER
@router.post("/")
def login(data: UserLogin):

    for u in get_users():
        # USER EXISTS IN IN_MEMORY_USER_LIST GENERATE JWT TOKEN
        if data.email == u.email and data.password == u.password :
            payload = {
                "user_id":u.user_id,
                "user_name": u.user_name,
                "role":"student"
            }

            token = create_token(payload)

            logger.info("Token Created Successfully | user_id={} | role=student",
                        u.user_id)

            return {
                "success": True,
                "token": token
            }

    for  a in get_admins():
        # ADMIN_USER EXISTS IN IN_MEMORY_USER_LIST GENERATE JWT TOKEN
        if data.email == a.email and data.password == a.password:
            payload = {
                "user_id":a.user_id,
                "user_name": a.user_name,
                "role":"admin"
            }

            token = create_token(payload)
            logger.info("Token Created Successfully | user_id={} | role=admin",
                        u.user_id)
            return {
                "success": True,
                "token": token
            }

    raise HTTPException (status_code=404, detail="Invalid credentials")
