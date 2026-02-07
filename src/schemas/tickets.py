from pydantic import BaseModel ,Field
from typing import Optional
from enum import Enum

class Priority(str,Enum):
    """
        Each enum value behaves like a string
        Can be sent/received as JSON cleanly
        Swagger understands it perfectly
        e.g.,
           ->  Priority.low.value == "Low"
           ->  Priority.low.name  == "LOW"
    """
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

class Status(str,Enum):
    OPEN = 'open'
    IN_PROGRESS = 'in progress'
    RESOLVED = 'resolved'


class CreateTicketsStudent(BaseModel):
    title : str =  Field(...,)                      # REQUIRED FIELD
    desc : str = Field(...,)                        # REQUIRED FIELD


class UpdateTicketByStaff(BaseModel):

      priority : Priority = Field(...,description="high, medium, low")
      status : Status = Field(...,description="open, in progress, resolved")