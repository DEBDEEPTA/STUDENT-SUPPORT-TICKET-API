from typing import List, Dict
from schemas.tickets import Status , Priority
from utils.generators.ticket_id_generator import get_ticket_id
# in-memory storage
tickets: List[Dict] = []


def add_ticket(title : str,
               description : str,
               priority : Priority,
               status : Status,
               user_id: str,
               user_name : str) -> Dict:
    """
    Create and store a new ticket
    """

    ticket = {
        "id": get_ticket_id(),
        "title": title,
        "description": description,
        "priority": priority,
        "status": status,
        "user_id": user_id,
        "user_name": user_name
    }

    tickets.append(ticket)
    return ticket


def get_all_tickets() -> List[Dict]:
    return tickets


def get_ticket_by_id(ticket_id: str, user_id: str) -> Dict | None:
    for ticket in tickets:
        if ticket["id"] == ticket_id and ticket["user_id"] == user_id :
            return ticket

    return None


def get_ticket_by_id_admin(ticket_id: str) -> Dict | None:
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    return None


def update_ticket_status_by_admin(ticket_id: str, status: Status, priority:Priority) -> Dict | None:
    ticket = get_ticket_by_id_admin(ticket_id)
    if not ticket:
        return  None

    ticket["status"] = status
    ticket["priority"] = priority
    return ticket

