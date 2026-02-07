
import uuid
def get_ticket_id():

    """
        uuid.uuid4() -> generates random uuid, e.g,-> f47ac10b-58cc-4372-a567-0e02b2c3d479
        .hex -> removes hyphens from the uuid, e.g,-> f47ac10b58cc4372a5670e02b2c3d479
        [:10] -> slice to 10 characters, e.g, ->  97a5b85a5b
        upper(), e.g, -> 97A5B85A5B
    """

    ticket_id = f"TKT-{uuid.uuid4().hex[:10].upper()}"
    return ticket_id




if __name__=="__main__":
    print(get_ticket_id())