from soldier_manager import add_solidier, remove_soldier, get_all_soldiers


def show_menu() -> None:
    print('\n=== Soldiers Duty Management ===\n')
    print('  1. Add soldier.')
    print('  2. Remove soldier.')
    print('  3. View all soldiers.')
    print('  4. Add duty.')
    print('  5. Update duty status.')
    print('  6. View sildier duties.')
    print('  0. Exit.')
    print('\n===*===*===*===*===*===*===*===*===\n')
show_menu()


def get_user_choice() -> str:
    return input('Enter your choice:\n>>> ')


def handle_add_soldier() -> None:
    soldier_id = int(input('Enter soldier ID:\n>>> '))
    soldier_name = input('Enter soldier name:\n>>> ')

    try:
        add_solidier(soldier_id, soldier_name)
        print('Soldier added successfully.')
    except (ValueError, KeyError) as e:
        print(f'Error: {e}')


def handle_remove_soldier() -> None:
    soldier_id = int(input('Enter soldier ID:\n>>> '))

    try:
        remove_soldier(soldier_id)
        print('Soldier removed successfully.')
    except (ValueError, KeyError) as e:
        print(f'Error: {e}')


def handle_view_soldiers() -> None:
    soldiers = get_all_soldiers()

    if not soldier:
            print('No soldiers.')
            return
    
    for soldier in soldiers.items():
        print(f'{soldier[0]}: {soldier[1]}')


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    pass


def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    pass
