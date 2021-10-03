import csv
import os
import platform

file = 'Contacts.csv'

def main_menu():
    print(f"{'='*10}Phone Book{'='*10}")
    print('A simple program to save and manage contact lists in the phone book.\n')
    print(f"{'='*10}Main Menu{'='*10}")
    print('[1] Show Contact')
    print('[2] Add Contact')
    print('[3] Update Contact')
    print('[4] Search Contact')
    print('[5] Delete Contact')
    print('[0] Exit')

    selected_number = str(input('\nInput number to select menu: '))
    if selected_number == '1':
        pass
    elif selected_number == '2':
        pass
    elif selected_number == '3':
        pass
    elif selected_number == '4':
        pass
    elif selected_number == '5':
        pass
    elif selected_number == '0':
        pass
    else:
        print('\nUnknown command.\n')

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def back_to_main_menu():
    input('Press enter to return to the main menu...')
    clear_screen()
    main_menu()

if __name__ == '__main__':
    main_menu()