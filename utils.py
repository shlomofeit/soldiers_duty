from data import soldiers, VALID_DAYS, VALID_STATUSES


def is_vaild_day(day: str) -> bool:
    return day in VALID_DAYS


def is_valid_name(name: str) -> bool:
    return name != ''


def is_valid_status(status: str) -> bool:
    return status in VALID_STATUSES


def find_soldier_by_id(id: int) -> dict:
    for i in soldiers:
        if i['id'] == id:
            return i    

    return None

def find_duty_by_name(duties: list, name: str):
    for i in duties:
        if i['name'] == name:
            return i
    
    return None