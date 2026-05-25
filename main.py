from soldier_manager import add_solidier, remove_soldier, get_all_soldiers
from duty_manager import add_duty_to_soldier, update_duty_status, get_soldier_duties
import time


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


def get_user_choice() -> str:
    return input('Enter your choice:\n>>> ')


def handle_add_soldier() -> None:
    soldier_id = int(input('Enter soldier ID:\n>>> '))
    soldier_name = input('Enter soldier name:\n>>> ')
    time.sleep(1)

    try:
        add_solidier(soldier_id, soldier_name)
        print('Soldier added successfully.')
    except (ValueError, KeyError) as e:
        print(f'Error: {e}')


def handle_remove_soldier() -> None:
    soldier_id = int(input('Enter soldier ID:\n>>> '))
    time.sleep(1)

    try:
        remove_soldier(soldier_id)
        print('Soldier removed successfully.')
    except (ValueError, KeyError) as e:
        print(f'Error: {e}')


def handle_view_soldiers() -> None:
    soldiers = get_all_soldiers()
    time.sleep(1)

    if not soldiers:
            print('No soldiers.')
            return
    
    for soldier in soldiers:
        print(f"{soldier['id']} - {soldier['name']}")


def handle_add_duty() -> None:
    soldier_id = int(input('Enter oldier ID:\n>>> '))
    duty_name = input('Enter duty name:\n>>> ')
    day = input('Enter the duty day:\n>>> ')
    time.sleep(1)
    
    try:
        add_duty_to_soldier(soldier_id, duty_name, day)
        print(f'The duty added successfully:\n')
        print(f' * Soldier ID: {soldier_id}')
        print(f' * Duty name: {duty_name}')
        print(f' * Day: {day}')
        print(f' * Status: Pending')

    except (ValueError, KeyError) as e:
        print(f'Error: {e}')


def handle_update_duty_status() -> None:
    soldier_id = int(input('Enter oldier ID:\n>>> '))
    duty_name = input('Enter duty name:\n>>> ')
    new_status = input('Enter new status:\n>>> ')
    time.sleep(1)
    
    try:
        update_duty_status(soldier_id, duty_name, new_status)
        print(f'The duty updated successfully:\n')
        print(f' * Soldier ID: {soldier_id}')
        print(f' * Duty name: {duty_name}')
        print(f' * New status: {new_status}')
        
    except (ValueError, KeyError) as e:
        print(f'Error: {e}')


def handle_view_soldier_duties() -> None:
    soldier_id = int(input('Enter oldier ID:\n>>> '))
    time.sleep(1)

    try:
        duty = get_soldier_duties(soldier_id)
        for i in duty:
            print(i['name'])
            print(i['day'])
            print(i['status'])
            print('=====\n')

    except (ValueError, KeyError) as e:
        print(f'Error: {e}')


def main() -> None:
    while True:
        show_menu()
        choice = get_user_choice()
        print('')

        if choice == '1':
            handle_add_soldier()
        elif choice == '2':
            handle_remove_soldier()
        elif choice == '3':
            handle_view_soldiers()
        elif choice == '4':
            handle_add_duty()
        elif choice == '5':
            handle_update_duty_status()
        elif choice == '6':
            handle_view_soldier_duties()
        elif choice == '0':
            break
        else:
            print('Invalid Choice. pls try again.\n\n')
        time.sleep(1)


if __name__ == '__main__':
    main()