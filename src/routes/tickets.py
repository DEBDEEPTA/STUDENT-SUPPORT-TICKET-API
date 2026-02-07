from fastapi import APIRouter, Depends, HTTPException, Path
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils.jwt_handaler import verify_token
from schemas.tickets import CreateTicketsStudent, UpdateTicketByStaff
from in_memory_db.in_memory_tickets.tickets_db import add_ticket, get_all_tickets,get_ticket_by_id, get_ticket_by_id_admin,update_ticket_status_by_admin

from schemas.tickets import Status, Priority
from utils.logger import logger

router = APIRouter()
security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    payload = verify_token(credentials.credentials)

    if  not payload:
        raise HTTPException (status_code=401, detail="invalid token")
    return payload


@router.post("/create")
def create_ticket(data: CreateTicketsStudent, user = Depends(get_current_user)):

    logger.info("Creating ticket | user_id={}", user['user_id'])

    ticket = add_ticket(
        title= data.title,
        description= data.desc,
        priority= Priority.MEDIUM,
        status= Status.OPEN,
        user_id=user["user_id"],
        user_name=user["user_name"]
    )
    return {
        "success": True,
        "ticket": ticket
    }

@router.get("/all")
def get_tickets(user = Depends(get_current_user)):
    current_user = user["user_id"]
    all_tickets = get_all_tickets()
    user_ticket_list = []

    role = user["role"]
    if role == "admin":
        logger.info("Fetching All Admin Tickets | user_id={}",user['user_id'])
        user_ticket_list = all_tickets

    if role == "student":
        logger.info("Fetching All Students Tickets | user_id={}", user['user_id'])

        for ticket in  all_tickets:
            if ticket["user_id"] == current_user:
                user_ticket_list.append(ticket)

    return user_ticket_list


@router.get("/{ticket_id}")
def get_ticket(ticket_id : str = Path(description="Ticket ID"),
               user = Depends(get_current_user)):


    logger.info("Fetching Ticket By ID | ticket_id={}",
                ticket_id,)

    role = user["role"]
    ticket = None

    if role == "admin":
        ticket = get_ticket_by_id_admin(ticket_id=ticket_id)
    if role == "student":
        user_id = user["user_id"]
        ticket = get_ticket_by_id(ticket_id = ticket_id,user_id=user_id)

    if ticket:
        logger.success("Ticket Found | ticket_id={}",ticket_id)
    else:
        logger.error("Ticket Not Found | ticket_id={}",ticket_id)

    return ticket


@router.post("/update/{ticket_id}")
def update_ticket(*,ticket_id : str = Path(description="Ticket ID Which Needs To Be Updated"),
                  data : UpdateTicketByStaff,
                  user = Depends(get_current_user)):

    logger.info("Admin updating ticket | ticket_id={} | status={} | priority={}",
        ticket_id, data.status, data.priority
                )

    role = user["role"]

    if role == "admin":
        status = data.status
        priority = data.priority

        ticket = update_ticket_status_by_admin(ticket_id=ticket_id,status=status,priority=priority)

        if not ticket:
            return {
                "message": "No tickets Found",
                "tickets": ticket
            }
        logger.success("Admin Updated Ticket Successfully | ticket_id={} | status={} | priority={}",
                      ticket_id, data.status, data.priority)

        return ticket







