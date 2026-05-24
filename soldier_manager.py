from data import soldiers
from utils import find_duty_by_name, find_soldier_by_id, is_valid_name

def add_solidier(soldier_id: int, name: str):
    if find_soldier_by_id(soldier_id):
        raise ValueError('ID in use already.')
    
    if not is_valid_name(name):
        raise ValueError('Name must be correct name.')
    
    soldiers.append({
        'id': soldier_id,
        'name': name,
        'duties': []
    })


def remove_soldier(soldier_id: int):
    if not find_soldier_by_id(soldier_id):
        raise ValueError('ID dont exist.')
    
    for index, soldier in enumerate(soldiers):
        if soldier['id'] == soldier_id:
            del soldiers[index]
            break