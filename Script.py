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

    //input is obtained as int
    
    selected_number = int(input('\nInput number to select menu: '))
    
    //changed the long else if condition to shorter to reduce the programming memory
    
    if selected_number in range (0,6):
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
