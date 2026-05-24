from data import soldiers, VALID_STATUSES
from utils import is_vaild_day, is_valid_name, is_valid_status, find_soldier_by_id, find_duty_by_name


def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    if not is_vaild_day(day):
        raise ValueError('Day must be Sunday-Thoursday.')
    
    soldier = find_soldier_by_id(soldier_id)

    if soldier is None:
        raise KeyError('ID does not exist.')
    
    if find_duty_by_name(soldier['duties'], duty_name):
        raise ValueError('This duty name already exist.')
    
    soldier['duties'].append({
        'name': duty_name,
        'day': day,
        'status': 'pending'
    })
    

def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    if not is_valid_status(new_status):
        raise ValueError(f'The {new_status} is not in the statuses list.')
    
    soldier = find_soldier_by_id(soldier_id)

    if soldier is None:
        raise KeyError('ID does not exist.')
    
    duty = find_duty_by_name(soldier['duties'], duty_name)

    if not duty:
        raise KeyError('This duty name does not exist.')
    
    duty['status'] = new_status


def get_soldier_duties(soldier_id: int) -> list:
    """
    מחזירה את רשימת התורנויות של חייל.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
    
    מחזירה:
        list: רשימת תורנויות (מילונים)
              רשימה ריקה אם אין תורנויות
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    גישה מבוקרת לתורנויות של חייל.
    מפרידה בין הנתונים לבין הגישה אליהם.
    זורקת exception אם החייל לא קיים (במקום להחזיר רשימה ריקה).
    """
    pass